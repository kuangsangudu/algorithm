'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 22:07       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


class SegTree:
    def __init__(self, init, func, ide):
        self.n = len(init)
        self.func = func
        self.ide = ide
        self.size = 1 << (self.n - 1).bit_length()
        self.tree = [self.ide for i in range(2 * self.size)]
        for i in range(self.n):
            self.tree[self.size + i] = init[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i | 1])

    def update(self, k, x):
        k += self.size
        self.tree[k] = x
        k >>= 1
        while k:
            self.tree[k] = self.func(self.tree[2 * k], self.tree[k * 2 | 1])
            k >>= 1

    def get(self, i):
        return self.tree[i + self.size]

    def query(self, l, r):
        l += self.size
        r += self.size
        l_res = self.ide
        r_res = self.ide
        while l < r:
            if l & 1:
                l_res = self.func(l_res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_res = self.func(self.tree[r], r_res)
            l >>= 1
            r >>= 1
        return self.func(l_res, r_res)

    def debug(self, s=10):
        print([self.get(i) for i in range(min(self.n, s))])


def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    mod = 998244353
    tree = SegTree([0] * (N+1), lambda x, y: (x+y) % mod, 0)
    for i in range(N-1, 0, -1):
        d = pow(a[i-1], mod-2, mod)
        tree.update(i, (tree.query(i+1, i+a[i-1]+1) * d + 1 + d) % mod)
    print(tree.get(1))


def main1(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    mod = 998244353
    dp = [0] * N
    cum = [0] * (N + 1)
    inv = [pow(a, mod - 2, mod) for a in A]
    for i in range(N - 2, -1, -1):
        a = A[i]
        dp[i] = ((1 + cum[i + 1] - cum[i + a + 1] + a) * inv[i]) % mod
        cum[i] = (cum[i + 1] + dp[i]) % mod

    print(dp[0])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)