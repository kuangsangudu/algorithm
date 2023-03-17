'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/11 20:14       
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
    H, W = map(int, lines[0].split(" "))
    A = []
    for line in lines[1:]:
        A.append(list(map(int, line.split(" "))))
    visited = collections.defaultdict(dict)
    d = {}
    i = 0
    for row in A:
        for n in row:
            if d.get(n, -1) == -1:
                d[n] = 1 << i
                i += 1

    q = [[0, 0, d[A[0][0]]]]
    while q:
        i, j, s = q.pop()
        if i+j == H-1:
            visited[(i, j)][s] = visited[(i, j)].get(s, 0) + 1
            continue
        if i < H-1 and s & d[A[i+1][j]] == 0:
            q.append([i+1, j, s | d[A[i+1][j]]])
        if j < W-1 and s & d[A[i][j+1]] == 0:
            q.append([i, j+1, s | d[A[i][j+1]]])

    q = [[H-1, W-1, 0]]
    vis = collections.defaultdict(dict)
    ret = 0
    while q:
        i, j, s = q.pop()
        if i+j == H-1:
            vis[(i, j)][s] = vis[(i, j)].get(s, 0) + 1
            continue
        if s & d[A[i][j]]:
            continue
        s |= d[A[i][j]]
        if i > 0:
            q.append([i-1, j, s])
        if j > 0:
            q.append([i, j-1, s])

    for key, value in visited.items():
        for m in value.keys():
            for n in vis[key].keys():
                if m & n == 0:
                    ret += value[m] * vis[key][n]
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)