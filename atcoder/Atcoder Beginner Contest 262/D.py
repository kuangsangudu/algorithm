'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 21:20       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


def combination(m, n, mod):
    c = [[0] * (m+1) for _ in range(n+1)]
    c[0][0] = 1
    for i in range(1, m):
        c[i][0] = 1
        for j in range(1, n):
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod
    return c


# dp[j][k][l] the number of ways, modulo 998244353, to choose k terms from the first j terms of A such
# that the remainder by i of the sum of the chosen terms equals l
def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    mod = 998244353
    ret = 0

    for i in range(1, N+1):
        dp = [[[0] * i for _ in range(i+1)] for _ in range(N+1)]
        dp[0][0][0] = 1
        for j in range(N):
            for k in range(i+1):
                for l in range(i):
                    dp[j+1][k][l] += dp[j][k][l]
                    if k != i:
                        dp[j+1][k+1][(l+a[j]) % i] += dp[j][k][l]
        ret = (ret + dp[N][i][0]) % mod
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)