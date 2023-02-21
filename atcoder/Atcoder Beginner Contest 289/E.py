'''
@Project: algorithm
@Description: TODO
@Time:2023/02/14 16:20
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


def main():
    T = int(input())
    inf = float("inf")
    for _ in range(T):
        N, M = map(int, input().split(" "))
        C = list(map(int, input().split(" ")))
        g = [[] for _ in range(N+1)]
        for _ in range(M):
            u, v = map(int, input().split(" "))
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        if C[0] == C[-1]:
            print(-1)
            continue
        # bg = [[] for _ in range(N*N)]
        # for i in range(N):
        #     for j in range(N):
        #         if i == j or C[i] == C[j]:
        #             continue
        #         t = i * N + j
        #         for nxt_i in g[i]:
        #             for nxt_j in g[j]:
        #                 if C[nxt_j] != C[nxt_i]:
        #                     bg[t].append(nxt_i * N + nxt_j)

        q = collections.deque([[0, 0, N-1]])
        visited = {N - 1}
        target = (N-1) * N
        ret = -1
        while q:
            s, i, j = q.popleft()
            for nxt_i in g[i]:
                for nxt_j in g[j]:
                    if nxt_i == nxt_j or C[nxt_i] == C[nxt_j]:
                        continue
                    nxt = nxt_i * N + nxt_j
                    if nxt not in visited:
                        q.append([s+1, nxt_i, nxt_j])
                        visited.add(nxt)
                        if nxt == target:
                            ret = s+1
                            break
        print(ret)


if __name__ == '__main__':
    main()