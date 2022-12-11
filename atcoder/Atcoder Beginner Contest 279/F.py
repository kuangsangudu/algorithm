'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 21:40       
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

# ld[x]= the representative element of the set of balls contained in box x, or −1 if it is empty;
# ing[y]= the box that the set represented by y belongs to,
# or an indeterminate value if there is no set represented by y.


def main(lines):
    N, Q = map(int, lines[0].split(" "))
    a = list(range(1, N+1))
    union = Union(N+Q+1)
    ld = list(range(N+1))
    inv = list(range(N+1)) + [-1] * Q
    ball = N+1
    for line in lines[1:]:
        if line[0] == "1":
            _, x, y = map(int, line.split(" "))
            if ld[y] == -1:
                continue
            elif ld[x] == -1:
                ld[x] = ld[y]
                inv[ld[x]] = x
                ld[y] = -1
            else:
                union.union(ld[x], ld[y])
                ld[x] = union.find(ld[x])
                inv[ld[x]] = x
                ld[y] = -1

        elif line[0] == "2":
            _, x = map(int, line.split(" "))
            if ld[x] == -1:
                ld[x] = ball
                inv[ball] = x
            else:
                union.union(ld[x], ball)
                ld[x] = union.find(ld[x])
                inv[ball] = x
            ball += 1

        else:
            _, x = map(int, line.split(" "))
            par_x = union.find(x)
            print(inv[par_x])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


