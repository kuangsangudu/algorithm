'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 22:18       
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
from typing import List

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines: List[str]):
    H, W = map(int, lines[0].split(" "))
    A = []
    maps = []
    graph = [[] for _ in range(W)]
    in_deg = [0] * W
    for i, line in enumerate(lines[1:]):
        A.append(list(map(int, line.split(" "))))
        min_a, max_a = float("inf"), 0
        sum_a = collections.defaultdict(list)
        for j, num in enumerate(A[-1]):
            if num:
                sum_a[num].append(j)
                min_a = min(min_a, num)
                max_a = max(num, max_a)
        maps.append([min_a, max_a])

        keys = sorted(sum_a.keys())
        # Point the idx of the equal value to a new id(new_p), while the new id(new_p) points
        # to the next idx of the equal value
        for j in range(len(keys)-1):
            graph.append([])
            in_deg.append(0)
            new_p = len(graph)-1
            for idx in sum_a[keys[j]]:
                graph[idx].append(new_p)
                in_deg[new_p] += 1
            for idx in sum_a[keys[j+1]]:
                graph[new_p].append(idx)
                in_deg[idx] += 1

    maps.sort()
    pre_min, pre_max = 0, 0
    for i, (min_num, max_num) in enumerate(maps):
        if min_num < pre_max:
            print("No")
            return
        pre_min, pre_max = min_num, max_num

    q = []
    for i in range(W):
        if in_deg[i] == 0:
            q.append(i)

    while q:
        n = q.pop()
        for nxt in graph[n]:
            if in_deg[nxt] > 0:
                in_deg[nxt] -= 1
                if in_deg[nxt] == 0:
                    q.append(nxt)
    if sum(in_deg) == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)