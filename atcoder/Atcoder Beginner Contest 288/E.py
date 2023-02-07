'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/04 21:42       
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

sys.setrecursionlimit(10 ** 6)


# this lower bound is achievable. Indeed, it can be achieved by repeatedly buying the item whose current cost achieves
# the lower bound (1), with the maximum item number.
def main(lines):
    N, M = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    C = list(map(int, lines[2].split(" ")))
    X = set(map(int, lines[3].split(" ")))

    Inf = float("inf")
    # cost = [[Inf] * N for _ in range(N)]
    # for i, c in enumerate(C):
    #     cost[i][i] = c
    #     for j in range(i+1, N):
    #         cost[i][j] = min(cost[i][j-1], C[j])
    #
    # dp = [[Inf] * (N+1) for _ in range(N+1)]
    # dp[0][0] = 0
    # for i in range(N):
    #     for j in range(i, -1, -1):
    #         dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + cost[i-j][i]+A[i])
    #         if i+1 not in X:
    #             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    # print(min(dp[-1][len(X):]))

    dp = [Inf] * (N+1)
    dp[0] = 0
    for i in range(N):
        ndp = [Inf] * (N+1)
        c = C[i]
        for j in range(i+1):
            c = min(c, C[i-j])
            ndp[j+1] = min(ndp[j+1], dp[j] + c + A[i])
            if i+1 not in X:
                ndp[j] = min(ndp[j], dp[j])
        dp = ndp
    print(min(dp))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)