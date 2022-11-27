'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 22:50       
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
    N = int(lines[0])
    S = lines[1:]
    target = (1 << len(S)) - 1

    @functools.lru_cache(None)
    def dfs(last, status):
        if status == target:
            return False
        for nxt in range(len(S)):
            if (status >> nxt) & 1 == 0 and S[nxt][0] == S[last][-1] and not dfs(nxt, status | (1 << nxt)):
                return True
        return False

    for i in range(len(S)):
        if not dfs(i, 1 << i):
            print("First")
            return
    print("Second")


def main1(lines):
    N = int(lines[0])
    S = lines[1:]
    target = (1 << len(S)) - 1
    dp = [[False] * N for _ in range(1 << N)]
    for i in range(target, -1, -1):
        for j in range(N):
            if (i >> j) & 1 == 0:
                continue
            for nxt in range(N):
                if (i >> nxt) & 1 == 0 and S[j][-1] == S[nxt][0] and not dp[i | (1 << nxt)][nxt]:
                    dp[i][j] = True
                    break

    for i in range(len(S)):
        if not dp[1 << i][i]:
            print("First")
            return
    print("Second")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)
