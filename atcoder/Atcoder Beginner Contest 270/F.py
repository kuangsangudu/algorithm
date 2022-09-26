'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/26 11:55       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


class Union:
    def __init__(self, lens):
        self.Union = list(range(lens))
        self.rank = [1] * lens
        self.nums = lens-1

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
        self.nums -= 1

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N, M = map(int, lines[0].split(" "))
    X = list(map(int, lines[1].split(" ")))
    Y = list(map(int, lines[2].split(" ")))
    Z = [list(map(int, line.split(" "))) for line in lines[3:]]
    ret = float("inf")

    # Consider whether to build an airport or port, use binary to represent various situations
    for i in range(4):
        lens = N
        arr = []
        if i & 1:
            for j, n in enumerate(X, start=1):
                arr.append([j, lens+1, n])
            lens += 1
        if i & 2:
            for j, n in enumerate(Y, start=1):
                arr.append([j, lens+1, n])
            lens += 1

        union = Union(lens + 1)
        arr = sorted(arr + Z, key=lambda x: x[2])
        sums = 0
        for m, n, dis in arr:
            if union.nums == 1:
                break
            if union.is_union(m, n):
                continue
            sums += dis
            union.union(m, n)

        if union.nums == 1:
            ret = min(ret, sums)

    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)