'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/24 21:22       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    N, K = map(int, lines[0].split(" "))
    a = list(map(int, lines[1].split(" ")))
    dp = [[float("-inf"), float("-inf")] for _ in range(N+1)]
    dp[0] = [0, 0]
    for i in range(len(dp)):
        for nxt in a:
            if i + nxt <= N:
                dp[i+nxt][0] = max(dp[i+nxt][0], -dp[i][1]+nxt)
                dp[i+nxt][1] = max(dp[i+nxt][1], -dp[i][0]+nxt)
    print((N-dp[-1][0])//2 + dp[-1][0])


def main1(lines):
    N, K = map(int, lines[0].split(" "))
    a = list(map(int, lines[1].split(" ")))
    dp = [0 for _ in range(N+1)]
    for i in range(len(dp)):
        for j in a:
            if j > i:
                continue
            dp[i] = max(dp[i], i - dp[i-j])
    print(dp[-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)