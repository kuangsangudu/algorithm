'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/29 22:13       
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
    N, M = map(int, lines[0].split(" "))
    a = list(map(int, lines[1].split(" ")))
    inf = M+1
    dp = [[inf] * 2 for _ in range(M+1)]
    dp[0][1] = 0
    for i in range(1, N+1):
        for j in range(M, -1, -1):
            for k, n in enumerate(dp[j]):
                if n != inf:
                    if a[i - 1] + j <= M:
                        dp[a[i - 1]+j][1] = min(dp[a[i - 1]+j][1], n)

            dp[j][0] = min(dp[j][0], dp[j][1]+1)
            dp[j][1] = inf
            if dp[j][0] > inf:
                dp[j][0] = inf

    for row in dp[1:]:
        print(min(row) if min(row) != inf else -1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)