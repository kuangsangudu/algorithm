'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/04 22:11       
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


def main(lines):
    N = int(lines[0])
    X = int(lines[1])
    s = str(X)
    mod = 998244353

    dp = [0] * (N+1)
    pres = 0
    for i, n in enumerate(s):
        dp[i+1] = 10 * dp[i] + (pres+1) * int(n)
        dp[i+1] %= mod
        pres += dp[i+1]
        pres %= mod
    print(dp[-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)