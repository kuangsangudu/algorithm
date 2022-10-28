'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/22 22:22       
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


def t(i, j, m, n):
    return (math.pow(i - m, 2) + math.pow(j - n, 2)) ** 0.5


# dp problem
def main(lines):
    N, M = map(int, lines[0].split(" "))
    alls = [list(map(int, line.split(" "))) for line in lines[1:]]
    target = (1 << N) - 1
    r = (1 << (N + M)) - (1 << N)

    pre_sum = [[0.0] * (N+M) for _ in range(N+M)]
    for i in range(N+M):
        for j in range(i, N+M):
            pre_sum[i][j] = t(alls[i][0], alls[i][1], alls[j][0], alls[j][1])
            pre_sum[j][i] = pre_sum[i][j]

    dp = [[float("inf")] * (1 << (len(alls))) for _ in range(N+M)]
    dp[0][0] = 0
    ret = float("inf")
    for i in range(N + M):
        dp[i][1 << i] = t(0, 0, alls[i][0], alls[i][1])
        if (1 << i) & target == target:
            ret = min(ret, dp[i][1 << i] * 2)

    for i in range(1, len(dp[0])):
        for j in range(N + M):
            if (i >> j) & 1:
                s = bin(i & r)[2:]
                speed = 1 << s.count("1")
                for p in range(N + M):
                    if (i >> p) & 1 == 0:
                        nxt = i + (1 << p)
                        new_dis = dp[j][i] + pre_sum[j][p]/speed
                        dp[p][nxt] = min(dp[p][nxt], new_dis)
                        if nxt & target == target:
                            ss = speed * 2 if p >= N else speed
                            ret = min(ret, new_dis + t(0, 0, alls[p][0], alls[p][1])/ss)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)