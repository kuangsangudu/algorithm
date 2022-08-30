'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/29 23:38       
@Author:ZHANG               
 
'''
import collections
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


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


# it can also use Inclusion-exclusion principle to solve this problem.
def main(lines):
    R, G, B, K = map(int, lines[0].split(" "))
    R -= K
    G -= K
    sums = R+G+B+K
    mod = 998244353
    c = Combination(sums, mod)
    ret = c.C(G+B+K, K) * c.C(G+B, B) * c.C(R+K+B, K+B) % mod
    # Inclusion-exclusion principle
    # ret = 0
    # for i in range(min(R, G)+1):
    #     ret = (ret + c.C(sums-i, K) * c.C(sums-i-K, B) * c.C(sums-i-K-B, R-i) * c.C(G, G-i) * (-1 if i % 2 else 1)) % mod
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)