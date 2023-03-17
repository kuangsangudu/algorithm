'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/11 20:07       
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
    vis = [False] * (N+1)
    for i, n in enumerate(A):
        if not vis[i+1]:
            vis[n] = True

    newA = [i+1 for i, n in enumerate(vis[1:]) if not n]
    print(len(newA))
    print(*newA)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)