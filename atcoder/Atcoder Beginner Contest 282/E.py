'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/17 21:44       
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
    A = list(map(int, lines[1].split(" ")))
    union = Union(N)
    queue = []
    for i in range(N):
        for j in range(i+1, N):
            num = (pow(A[i], A[j], M) + pow(A[j], A[i], M)) % M
            heapq.heappush(queue, [-num, i, j])

    ret = 0
    while queue:
        s, i, j = heapq.heappop(queue)
        if union.is_union(i, j):
            continue
        else:
            union.union(i, j)
            ret -= s
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
