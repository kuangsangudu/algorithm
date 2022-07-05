'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/2 21:37       
@Author:ZHANG               
 
'''
import bisect
import sys


def main(lines):
    N, Q, X = map(int, lines[0].split(" "))
    W = list(map(int, lines[1].split(" "))) * 2
    C = [0] * N
    ano, X = divmod(X, sum(W) // 2)
    ano *= N
    sums, j = 0, 0
    for i in range(N):
        while j < len(W) and sums < X:
            sums += W[j]
            j += 1
        C[i] = j-i
        sums -= W[i]

    re = {}
    nxt = 0
    i = 1
    visited = [0] * N
    while not visited[nxt]:
        re[i] = C[nxt]
        visited[nxt] = i
        nxt = (nxt + C[nxt]) % N
        i += 1
    # cycle means cycle length, cycleidx means the cycle num's idx
    cycle = i - visited[nxt]
    cycleidx = visited[nxt]
    print(re, cycle, cycleidx)
    for q in lines[2:]:
        idx = int(q)
        if idx <= cycleidx:
            print(re[idx] + ano)
        else:
            print(re[(idx-cycleidx) % cycle + cycleidx] + ano)


def main1(lines):
    N, Q, X = map(int, lines[0].split(" "))
    W = list(map(int, lines[1].split(" ")))
    sums = [0] * N
    sums[0] = W[0]
    for i, num in enumerate(W[1:], start=1):
        sums[i] = sums[i-1] + num
    ano, X = divmod(X, sums[-1])
    ano *= N
    re = []
    start = 0
    idx = 0
    visited = {}
    for i in range(N):
        start += X
        alls = 0
        nums = 0
        if start >= sums[-1]:
            start -= sums[-1]
            alls += sums[-1] - sums[idx-1]
            nums += N - idx + 1
            j = bisect.bisect_left(sums, start)
            alls += sums[j]
            nums += j
        else:
            j = bisect.bisect_left(sums, start)
            alls += (sums[j] - sums[idx-1] if idx >= 1 else sums[j])
            nums += j - idx + 1
        start += alls - X
        visited[idx] = i
        idx = (j + 1) % N
        re.append(nums + ano)
        if idx in visited:
            cycle = visited[idx]
            break

    cyclenum = len(re) - cycle
    for q in lines[2:]:
        idx = int(q) - 1
        if idx <= cycle:
            print(re[idx])
        else:
            print(re[(idx-cycle) % cyclenum + cycle])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    # main(lines)
    main1(lines)
