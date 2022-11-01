'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/29 21:05       
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


def dis(a, b):
    return (a[0]-b[0]) ** 2 + (a[1]-b[1])**2


def conf(ab, ad, cd, bc, ac, bd):
    return ab == ad == cd == bc and ac == bd


def main(lines):
    re = []
    for i, row in enumerate(lines):
        for j, n in enumerate(row):
            if n == "#":
                re.append((i, j))

    ret = 0
    for a, b, c, d in itertools.combinations(re, 4):
        ab = dis(a, b)
        ac = dis(a, c)
        ad = dis(a, d)
        bd = dis(b, d)
        bc = dis(b, c)
        cd = dis(c, d)
        if ab == ac:
            if conf(ab, ac, cd, bd, ad, bc):
                ret += 1
        elif ab == ad:
            if conf(ab, ad, cd, bc, ac, bc):
                ret += 1
        elif ac == ad:
            if conf(ac, ad, bc, bd, cd, ab):
                ret += 1

    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)