'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/11 20:55       
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


class Union:
    def __init__(self, lens):
        self.Union = list(range(lens))
        self.rank = [1] * lens
        self.nums = lens

    def find(self, x):
        while self.Union[x] != x:
            x = self.Union[x]
        return x

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x
        self.rank[par_x] += self.rank[par_y]
        self.Union[par_y] = par_x
        self.nums -= 1
        return False

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N, M = map(int, lines[0].split(" "))
    union = Union(N+1)
    l = 0
    for line in lines[1:]:
        a, b, c, d = line.split(" ")
        a, c = int(a), int(c)
        if union.union(a, c):
            l += 1

    print(l, union.nums-1-l)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)