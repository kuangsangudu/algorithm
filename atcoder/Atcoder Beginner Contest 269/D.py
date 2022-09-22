'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 21:12       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


class Union:
    def __init__(self, lens, n):
        self.Union = list(range(lens))
        self.rank = [1] * lens
        self.n = n

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
        self.n -= 1

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N = int(lines[0])
    union = Union(2000 * 2000 + 2001, N)
    maps = {}
    for line in lines[1:]:
        x, y = map(int, line.split(" "))
        maps[(x, y)] = 1
        for nx, ny in [[x-1, y-1], [x-1, y], [x, y-1], [x, y+1], [x+1, y], [x+1, y+1]]:
            if maps.get((nx, ny), -1) != -1:
                union.union((x+1000)*2000 + y+1000, (nx+1000)*2000 + ny+1000)
    print(union.n)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)