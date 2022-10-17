'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 22:30       
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
    N, X = map(int, lines[0].split(" "))
    Y = list(map(int, lines[1].split(" ")))
    Z = list(map(int, lines[2].split(" ")))

    sort_arr = sorted(Z+Y+[0, X])
    val2idx = collections.defaultdict(int)
    start, end = -1, -1
    for i, n in enumerate(sort_arr):
        val2idx[n] = i
        if n == 0:
            start = i
        if n == X:
            end = i

    walls = [-1] * len(sort_arr)
    walls[start] = 0
    for i, n in enumerate(Y):
        walls[val2idx[n]] = i

    l, r = start, start
    while True:
        flag = False
        while l - 1 >= 0 and walls[l-1] == -1:
            walls[l-1] = walls[l] + sort_arr[l] - sort_arr[l-1]
            l -= 1
            flag = True
        while r + 1 < len(sort_arr) and walls[r+1] == -1:
            walls[r+1] = walls[r] + sort_arr[r+1] - sort_arr[r]
            r += 1
            flag = True

        if l > 0:
            hammer = val2idx[Z[walls[l-1]]]
            if walls[hammer] != -1:
                walls[l-1] = max(walls[l] + sort_arr[l] - sort_arr[l-1], walls[hammer] + sort_arr[hammer]-sort_arr[l-1])
                flag = True
                l -= 1

        if r + 1 < len(sort_arr):
            hammer = val2idx[Z[walls[r+1]]]
            if walls[hammer] != -1:
                walls[r+1] = max(walls[r] + sort_arr[r+1] - sort_arr[r], walls[hammer] + sort_arr[r+1]-sort_arr[hammer])
                flag = True
                r += 1

        if not flag:
            break
        if walls[end] != -1:
            print(walls[end])
            return

    print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)






