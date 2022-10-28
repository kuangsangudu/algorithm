'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/23 0:25       
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


def main(lines):
    N, A = map(int, lines[0].split())
    fish = [list(map(int, line.split())) for line in lines[1:]]
    ret = 0
    for w1, x1, v1 in fish:
        weights = collections.defaultdict(int)
        for w, x, v in fish:
            if v == v1:
                if x1 <= x <= x1+A:
                    weights[0] += w
            else:
                l, r = (x1-x)*10**9/(v-v1), (x1+A-x)*10**9/(v-v1)
                if l > r:
                    l, r = r, l
                if r >= 0:
                    weights[max(0, l)] += w
                    weights[r+1] -= w

        sums = 0
        for key in sorted(weights.keys()):
            sums += weights[key]
            ret = max(ret, sums)
    print(ret)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
