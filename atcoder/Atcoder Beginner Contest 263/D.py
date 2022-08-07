'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 21:42       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, L, R = map(int, lines[0].split(" "))
    a = list(map(int, lines[1].split(" ")))
    re = [0] * N
    re[-1] = min(a[-1], R)
    for i in range(N-2, -1, -1):
        re[i] = min(re[i+1] + a[i], R * (N-i))

    r = [0] * N
    r[0] = min(a[0], L)
    ret = re[0]
    for i in range(1, N):
        r[i] = min(r[i-1] + a[i], L * (i+1))
        ret = min(r[i] + (re[i+1] if i+1 < N else 0), ret)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)