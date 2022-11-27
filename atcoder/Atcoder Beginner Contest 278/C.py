'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 21:17       
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
    N, Q = map(int, lines[0].split(' '))
    maps = collections.defaultdict(set)
    for line in lines[1:]:
        t, a, b = map(int, line.split(" "))
        if t == 1:
            maps[a].add(b)
        elif t == 2:
            if maps.get(a, -1) != -1 and b in maps[a]:
                maps[a].remove(b)
        elif b in maps[a] and a in maps[b]:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
