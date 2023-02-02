'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 21:08       
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


class Union:
    def __init__(self, lens):
        self.Union = list(range(lens))
        self.rank = [1] * lens

    def find(self, x):
        while self.Union[x] != x:
            x = self.Union[x]
        return x

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return
        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x
        self.rank[par_x] += self.rank[par_y]
        self.Union[par_y] = par_x

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N, M = map(int, lines[0].split(" "))
    union = Union(N+1)
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        if union.is_union(u, v):
            print("No")
            return
        union.union(u, v)

    t = union.find(1)
    for i in range(2, N+1):
        if union.find(i) != t:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)