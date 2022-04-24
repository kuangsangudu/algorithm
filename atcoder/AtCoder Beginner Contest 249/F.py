'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/24 1:31       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq


# dp TLC
def main1(lines):
    N, K = list(map(int, lines[0].split(" ")))
    arr = []
    for i in range(N):
        arr.append(list(map(int, lines[i+1].split(" "))))
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(K, -1, -1):
            if j < K:
                dp[i][j + 1] = max(dp[i-1][j], dp[i][j + 1])
            if arr[i-1][0] == 1:
                dp[i][j] = arr[i-1][1]
            else:
                dp[i][j] = arr[i-1][1] + dp[i-1][j]
    print(max(dp[-1]))


# another method TLC
def main2(lines):
    N, K = list(map(int, lines[0].split(" ")))
    arr = []
    ones = [0]
    for i in range(N):
        arr.append(list(map(int, lines[i+1].split(" "))))
        if arr[-1][0] == 1:
            ones.append(i)
    ones.append(N)
    i = len(ones)-2
    re = []
    for j in range(ones[i]+1, ones[-1]):
        heapq.heappush(re, arr[j][1])
    ret = float('-inf')
    if K == 0:
        ret = sum([j for i, j in arr])
    while K:
        r = []
        k = K
        while k and re and re[0] < 0:
            k -= 1
            r.append(heapq.heappop(re))
        ret = max(ret, sum(re)+arr[ones[i]][1])
        K -= 1
        i -= 1
        for n in r:
            heapq.heappush(re, n)
        if i >= 0:
            for j in range(ones[i]+1, ones[i+1]):
                heapq.heappush(re, arr[j][1])

    print(ret)


# AC
def main(lines):
    N, K = list(map(int, lines[0].split(" ")))
    t = [0] * (N + 1)
    y = [0] * (N + 1)
    t[0] = 1
    for i in range(1, N + 1):
        t[i], y[i] = map(int, lines[i].split())
    ret = float("-inf")
    sums = 0
    re = []
    for i in range(N, -1, -1):
        if t[i] == 2:
            if y[i] >= 0:
                sums += y[i]
            else:
                heapq.heappush(re, -y[i])
        else:
            if K < 0:
                break
            ret = max(ret, sums+y[i])
            K -= 1
        if re and len(re) > K:
            sums -= heapq.heappop(re)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

