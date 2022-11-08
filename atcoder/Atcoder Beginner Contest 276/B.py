'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 11:10       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    N, M = map(int, lines[0].split(" "))
    maps = collections.defaultdict(list)
    for line in lines[1:]:
        a, b = map(int, line.split(" "))
        maps[a].append(b)
        maps[b].append(a)

    for i in range(1, N+1):
        maps[i].sort()
        print(*([len(maps[i])] + maps[i]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)