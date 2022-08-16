'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 21:38       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
import itertools
sys.setrecursionlimit(10 ** 6)
import functools


class Union:
    def __init__(self, lens, N):
        self.Union = list(range(lens))
        self.rank = [1] * lens
        self.w = [0] * lens
        for i in range(N+1, lens):
            self.w[i] = 1

    def find(self, x):
        while self.Union[x] != x:
            x = self.Union[x]
        return x

    def union(self, x, y):
        ret = 0
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return 0
        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x

        if self.w[par_x] ^ self.w[par_y] == 1:
            ret = self.rank[par_x] if self.w[par_x] == 0 else self.rank[par_y]
            self.w[par_x], self.w[par_y] = 1, 1
        self.rank[par_x] += self.rank[par_y]
        self.Union[par_y] = par_x
        return ret

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


# reverse thinking
def main(lines):
    N, M, E = map(int, lines[0].split(" "))
    U = []
    for line in lines[1:E+1]:
        U.append(list(map(int, line.split(" "))))
    Q = int(lines[E+1])
    X = list(map(int, lines[E+2:]))

    union = Union(N+M+1, N)
    v = set(X)
    ret = 0
    for i in range(len(U)):
        if i+1 in v:
            continue
        ret += union.union(U[i][0], U[i][1])

    re = []
    for i in range(len(X)-1, -1, -1):
        re.append(ret)
        ret += union.union(U[X[i]-1][0], (U[X[i]-1][1]))
    print(*re[::-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)