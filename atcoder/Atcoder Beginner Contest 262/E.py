'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 21:50       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def C(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        return self.C(n + r - 1, r - 1)


def main(lines):
    N, M, K = map(int, lines[0].split(" "))
    graph = collections.defaultdict(int)
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        graph[u] += 1
        graph[v] += 1

    even, odd = 0, 0
    for i in range(1, N+1):
        if graph[i] % 2:
            odd += 1
        else:
            even += 1

    mod = 998244353
    ret = 0
    c = Combination(N, mod)
    for i in range(0, K+1, 2):
        if i <= odd and K-i <= even:
            ret = (ret + c.C(odd, i) * c.C(even, K-i)) % mod
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
