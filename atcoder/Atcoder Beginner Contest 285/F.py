'''
@Project: algorithm
@Description: TODO
@Time:2023/01/16 11:47
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


class FenwickTree:
    def __init__(self, lens):
        self.arr = [0] * (lens + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= self.lowbit(i)
        return ret

    def update(self, i, num):
        while i < len(self.arr):
            self.arr[i] = self.arr[i] + num
            i += self.lowbit(i)

    def range_add(self, l, r, x):
        self.update(l, x)
        self.update(r + 1, -x)

    def range_get(self, l, r):
        return self.get(r) - self.get(l-1)


class Bit:
    def __init__(self, n, array=[]):
        """
        :param n: number of elements
        """
        self.n = n
        self.tree = [0]*(n+1)
        self.depth = n.bit_length() - 1
        for i, a in enumerate(array):
            self.add(i, a)

    def get(self,i):
        """ return summation of elements in [0,i) """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            # s%=MOD
            i = (i & (i + 1) )- 1
        return s

    def build(self, array):
        """ bulid BIT from array """
        for i, a in enumerate(array):
            self.add(i, a)

    def add(self, i, x):
        """ add x to i-th element """
        while i < self.n:
            self.tree[i] += x
            # self.tree[i]%=MOD
            i |= i + 1

    def get_range(self,i,j):
        """ return summation of elements in [i,j) """
        if i == 0:
            return self.get(j)
        return self.get(j)-self.get(i)

    def lower_bound(self, x, equal=False):
        """
        return tuple = (return maximum i s.t. a0+a1+...+ai < x (if not existing, -1 ) , a0+a1+...+ai )
        if one wants to include equal (i.e., a0+a1+...+ai <= x), please set equal = True
        (Cation) We must assume that A_i>=0
        """
        sum_ = 0
        pos = -1    # 1-indexed の時は pos = 0
        if not equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] < x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        if equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] <= x: # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        return pos, sum_

    def __getitem__(self, i):
        """ [a0, a1, a2, ...] """
        if i<0: i=self.n+i
        return self.get_range(i,i+1)

    def __setitem__(self, i, x):
        self.add(i,x-self[i])

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for i in range(self.n):
            yield self.get_range(i,i+1)

    def __str__(self):
        text1 = " ".join(["element:            "] + list(map(str, self)))
        text2 = " ".join(["cumsum(1-indexed):  "]+list(str(self.get(i)) for i in range(1,self.n+1)))
        return "\n".join((text1, text2))


# https://atcoder.jp/contests/abc285/submissions/38081674 not my method
def main(lines):
    N = int(lines[0])
    S = list(lines[1])
    Q = int(lines[2])
    S = [ord(s) - ord("a") for s in S]

    B = Bit(N + 1, [0] * (N + 1))

    T = [Bit(N) for _ in range(26)]

    for i in range(N):
        s = S[i]
        T[s][i] += 1

    for i in range(N - 1):
        if S[i] > S[i + 1]:
            B[i] = 1

    res = []
    for line in lines[3:]:
        q = line.split(" ")
        q[0] = int(q[0])
        if q[0] == 1:
            x = int(q[1])
            x -= 1
            c = ord(q[2]) - ord("a")
            if x > 0:
                if S[x - 1] <= c:
                    B[x - 1] = 0
                else:
                    B[x - 1] = 1
            if x + 1 < N:
                if c > S[x + 1]:
                    B[x] = 1
                else:
                    B[x] = 0
            T[S[x]][x] = 0
            S[x] = c
            T[c][x] = 1
        else:
            l = int(q[1])
            l -= 1
            r = int(q[2])
            f = 1
            if B.get_range(l, r - 1) > 0:
                f = 0
            else:
                a = S[l]
                b = S[r - 1]
                for s in range(a + 1, b):
                    if T[s].get_range(0, l) > 0 or T[s].get_range(r, N) > 0:
                        f = 0
            if f == 0:
                res.append("No")
            else:
                res.append("Yes")
    print(*res, sep="\n")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)