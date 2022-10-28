'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/22 21:06       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    maps = collections.defaultdict(int)
    maps[1] = 0
    for i, n in enumerate(A, start=1):
        maps[2*i] = maps[n] + 1
        maps[2 * i+1] = maps[n] + 1
    for i in range(1, 2*N+2):
        print(maps[i])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)