'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 21:09       
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


class Union:
    def __init__(self, lens):
        self.Union = {}
        self.rank = {}
        self.nums = lens-1

    def find(self, x):
        self.Union.setdefault(x, x)
        while self.Union[x] != x:
            x = self.Union[x]
        return x

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return
        self.rank.setdefault(par_x, 1)
        self.rank.setdefault(par_y, 1)
        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x
        self.rank[par_x] += self.rank[par_y]
        self.Union[par_y] = par_x
        self.nums -= 1

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N = int(lines[0])
    union = Union(N)
    for line in lines[1:]:
        a, b = map(int, line.split(" "))
        union.union(a, b)
    target = union.find(1)
    ret = 1
    for key in union.Union.keys():
        if union.find(key) == target:
            ret = max(ret, key)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)