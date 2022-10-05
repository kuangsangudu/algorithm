'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 22:01       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    def is_valid(i, j):
        if 0 <= i < N and 0 <= j < N:
            return True
        return False

    def dfs_up(i, j, num):
        if i + j == N-1:
            if mid[i].get(num, -1) == -1:
                mid[i][num] = 1
            else:
                mid[i][num] += 1
            return
        for ni, nj in [[i+1, j], [i, j+1]]:
            if is_valid(ni, nj):
                dfs_up(ni, nj, num ^ a[i][j])

    def dfs_down(i, j, num):
        nonlocal ret
        if i + j == N-1:
            ret += mid[i].get(num ^ a[i][j], 0)
            return
        for ni, nj in [[i-1, j], [i, j-1]]:
            if is_valid(ni, nj):
                dfs_down(ni, nj, num ^ a[i][j])

    N = int(lines[0])
    a = []
    maxs = 0
    for line in lines[1:]:
        a.append(list(map(int, line.split(" "))))
        maxs = max(maxs, max(a[-1]))

    mid = collections.defaultdict(dict)
    ret = 0
    dfs_up(0, 0, 0)
    dfs_down(N-1, N-1, 0)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)