'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 21:13       
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


def main(lines):
    N, K, D = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    dp = [[-1] * (D+1) for _ in range(K+2)]
    ret = -1
    for i in range(N):
        for j in range(K, -1, -1):
            for n in range(D):
                if dp[j][n] >= 0:
                    dp[j+1][(n+A[i]%D)%D] = max(dp[j+1][(n+A[i]%D)%D], dp[j][n] + A[i])
        dp[1][A[i] % D] = max(dp[1][A[i] % D], A[i])
        ret = max(ret, dp[K][0])

    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
