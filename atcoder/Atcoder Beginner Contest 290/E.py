'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/21 15:32       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import functools
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))

    total = 0
    l, r = 1, N
    while l < r:
        if l >= N+1-r:
            total += (r-l) * (N+1-r)
            r -= 1
        else:
            total += (r-l) * l
            l += 1

    g = collections.defaultdict(list)
    for i, n in enumerate(A, start=1):
        g[n].append(i)
    minus = 0
    for value in g.values():
        l, r = 0, len(value)-1
        while l < r:
            if value[l] >= N-value[r]+1:
                minus += (N-value[r]+1) * (r-l)
                r -= 1
            else:
                minus += value[l] * (r-l)
                l += 1
    print(total-minus)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)