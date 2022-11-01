'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/29 21:42       
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
    N, M, K = map(int, lines[0].split(" "))
    mod = 998244353
    m = pow(M, mod-2, mod)
    dp = [[0] * (N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j == N:
                dp[i][j] += dp[i-1][j]
                continue
            if dp[i-1][j] == 0:
                continue
            for k in range(1, M+1):
                if j + k <= N:
                    dp[i][j+k] = (dp[i][j+k] + dp[i-1][j] * m) % mod
                else:
                    dp[i][N - (j+k-N)] = (dp[i][N - (j+k-N)] + dp[i-1][j] * m) % mod

    print(dp[-1][N] % mod)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)