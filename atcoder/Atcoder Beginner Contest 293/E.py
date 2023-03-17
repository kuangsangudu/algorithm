'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/11 21:09       
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
    A, X, M = map(int, lines[0].split(" "))

    # 证明： https://kazun-kyopro.hatenablog.com/entry/ABC/293/E
    # def dfs(x):
    #     if x == 1:
    #         return 1 % M
    #     if x % 2:
    #         return (A * dfs(x-1) + 1) % M
    #     else:
    #         return dfs(x//2) * (1 + pow(A, x//2, M)) % M
    #
    # print(dfs(X))

    if A == 1:
        print(X % M)
    else:
        print((pow(A, X, M * (A - 1)) - 1) // (A - 1) % M) # 直接Mod M * （A-1）保证结果范围

    # https: // atcoder.jp / contests / abc293 / editorial / 5977， 采用分治的方法,将累积运算编程多换个变量之和


def mat_mul(a, b, mod):
    ret = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for s in range(len(a[0])):
                ret[i][j] += a[i][s] * b[s][j]
                ret[i][j] %= mod
    return ret


def mat_fast(a, x, mod):
    ret = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        ret[i][i] = 1

    while x:
        if x & 1:
            ret = mat_mul(ret, a, mod)
        a = mat_mul(a, a, mod)
        x >>= 1
    return ret


def main1(lines):
    A, X, M = map(int, lines[0].split(" "))
    a = [[A, 1], [0, 1]]
    print(mat_mul(mat_fast(a, X, M), [[0], [1]], M)[0][0])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)