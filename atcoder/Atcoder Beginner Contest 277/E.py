'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 21:32       
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
    N, M, K = map(int, lines[0].split(' '))
    maps = {0: collections.defaultdict(list), 1: collections.defaultdict(list)}
    for line in lines[1:M+1]:
        u, v, a = map(int, line.split(" "))
        maps[a][u].append(v)
        maps[a][v].append(u)

    if K > 0:
        s = collections.Counter(list(map(int, lines[-1].split(" "))))
    else:
        s = {}

    # Dijkstra
    # q = [[0, 1, 1]]
    # visited = [[float("inf"), float("inf")] for _ in range(N+1)]
    # visited[1][1] = 0
    # while q:
    #     sums, idx, status = heapq.heappop(q)
    #     for nxt in maps[status][idx]:
    #         if visited[nxt][status] > sums + 1:
    #             visited[nxt][status] = sums + 1
    #             heapq.heappush(q, [sums+1, nxt, status])
    #
    #     if s.get(idx, -1) != -1:
    #         for nxt in maps[status ^ 1][idx]:
    #             if visited[nxt][status ^ 1] > sums + 1:
    #                 visited[nxt][status ^ 1] = sums + 1
    #                 heapq.heappush(q, [sums + 1, nxt, status ^ 1])

    # 0-1 bfs
    q = collections.deque([[0, 1, 1]])
    visited = [[float("inf"), float("inf")] for _ in range(N+1)]
    visited[1][1] = 0
    while q:
        sums, idx, status = q.popleft()
        for nxt in maps[status][idx]:
            if visited[nxt][status] > sums + 1:
                visited[nxt][status] = sums + 1
                q.append([sums+1, nxt, status])

        if s.get(idx, -1) != -1:
            for nxt in maps[status ^ 1][idx]:
                if visited[nxt][status ^ 1] > sums + 1:
                    visited[nxt][status ^ 1] = sums + 1
                    q.append([sums + 1, nxt, status ^ 1])

    if min(visited[N]) != float("inf"):
        print(min(visited[N]))
    else:
        print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)