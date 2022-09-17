'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 22:19       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    P = list(map(int, lines[1].split(" ")))
    pos = {n: i for i, n in enumerate(P)}
    sk = [0] * (N+1)
    sb = [0] * (N+1)

    def add(l, r, k, b):
        if l > r:
            return
        sk[l] += k
        sk[r+1] -= k
        sb[l] += b
        sb[r+1] -= b

    for i in range(N):
        n = (pos[i] - i + N) % N
        if n < N//2:
            add(0, n-1, -1, n)
            add(n+1, n+N//2, 1, -n)
            add(n+N//2+1, N-1, -1, n+N)
        else:
            add(0, n-N//2-1, 1, N-n)
            add(n-N//2, n-1, -1, n)
            add(n, N-1, 1, -n)

    ret = float("inf")
    for i in range(N):
        if i > 0:
            sk[i] += sk[i-1]
            sb[i] += sb[i-1]
        ret = min(ret, sk[i] * i + sb[i])
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)