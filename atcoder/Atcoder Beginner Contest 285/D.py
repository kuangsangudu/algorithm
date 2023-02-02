'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/16 11:15       
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
    N = int(lines[0])
    S, T = [], []
    for line in lines[1:]:
        s, t = line.split(" ")
        S.append(s)
        T.append(t)

    arr = sorted(set(S+T))
    num2idx = collections.defaultdict(int)
    for i, n in enumerate(arr):
        num2idx[n] = i

    union = Union(len(arr))
    for i in range(len(S)):
        if union.is_union(num2idx[S[i]], num2idx[T[i]]):
            print("No")
            return
        union.union(num2idx[S[i]], num2idx[T[i]])
    print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)