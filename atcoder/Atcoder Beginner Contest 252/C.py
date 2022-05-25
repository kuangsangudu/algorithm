'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/21 21:06       
@Author:ZHANG               
 
'''
import sys
import heapq


def main1(lines):
    N = int(lines[0])
    S = lines[1:]
    dp = [0] * 11
    time = 0
    flag = False
    while True:
        visited = set()
        for l in S:
            visited.add(int(l[(time % 10)])+1)
        for j in visited:
            dp[j] += 1
            if dp[j] == N:
                print(time)
                flag = True
                break
        time += 1
        if flag:
            break


def main(lines):
    N = int(lines[0])
    S = lines[1:]
    ret = float("inf")
    for target in range(10):
        D = [0] * 10
        for j in range(N):
            D[S[j].index(str(target))] += 1
        t = 0
        for j in range(10):
            if D[j] == 0:
                continue
            t = max(t, 10 * (D[j] - 1) + j)
        ret = min(ret, t)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
