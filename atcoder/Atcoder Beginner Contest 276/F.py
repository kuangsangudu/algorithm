'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 21:59       
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
        self.tree[k] = self.func(self.tree[k], x)
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


# the idea is similar to https://atcoder.jp/contests/abc276/editorial/5188, but he use splay tree to solve the problem.
def main(lines):
    mod = 998244353
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))

    def Sum(a: int, b: int) -> int:
        return (a + b) % mod

    maxa = max(a)
    tree = SegTree([0] * (maxa+1), Sum, 0)
    tree1 = SegTree([0] * (maxa+1), Sum, 0)

    sums = 0

    for i in range(N):
        tree.update(a[i], a[i])
        tree1.update(a[i], 1)
        nums = tree1.query(0, a[i]+1)
        maxs = tree.query(0, maxa+1) - tree.query(0, a[i]+1)
        sums = (sums + maxs * 2 + (nums * 2-1)*a[i]) % mod
        print(sums * pow(i+1, mod-2, mod)**2 % mod)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)