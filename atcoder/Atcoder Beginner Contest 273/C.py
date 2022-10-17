'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 21:15       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    a = sorted(set(A), reverse=True)
    sums = 0
    maps = collections.defaultdict(int)
    for i, n in enumerate(a):
        maps[n] = sums
        sums += 1

    count = collections.Counter()
    for n in A:
        count[maps[n]] += 1
    for i in range(N):
        print(count[i])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)