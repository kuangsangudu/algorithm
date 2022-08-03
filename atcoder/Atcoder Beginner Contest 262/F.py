'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 22:01       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


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


# use segment tree to solve the sub array problem
def min_subarray(arr, k):
    lens = len(arr)
    n_arr = [n * lens + i for i, n in enumerate(arr)]
    tree = SegTree(n_arr, func=lambda x, y: x if x < y else y, ide=float("inf"))
    ret = []
    start = 0
    for i in range(k):
        mins = tree.query(start, lens-k+i+1)
        n, idx = divmod(mins, lens)
        ret.append(n)
        start = idx + 1
    return ret


# use sliding window
def min_sub_array(arr, k, rotation=0):
    q = []
    for i, e in enumerate(arr):
        while q and q[-1][0] > e:
            _, j = q[-1]
            if j < rotation:
                q.pop()
            elif k > 0:
                q.pop()
                k -= 1
            else:
                break
        q.append((e, i))
    while k > 0:
        q.pop()
        k -= 1
    return [t[0] for t in q]


def main1(lines):
    N, K = map(int, lines[0].split(" "))
    P = list(map(int, lines[1].split(" ")))

    ret = min_sub_array(P, K)

    if K > 0:
        idx = P.index(min(P[N-K:]))
        ret = min(ret, min_sub_array(P[idx:]+P[:idx], K-(N-idx), rotation=N-idx))

    print(*ret)


def main(lines):
    N, K = map(int, lines[0].split(" "))
    P = list(map(int, lines[1].split(" ")))
    head = []
    idx = N
    for i in range(N-K, N):
        while head and head[-1] > P[i]:
            head.pop()
        head.append(P[i])
        if len(head) == 1:
            idx = i

    remain = P[:idx]
    re_k = len(remain) - K + N - idx

    re_max = min_subarray(remain, re_k)
    for i in range(len(head)):
        if head[i] > re_max[0]:
            head = head[:i]
            break
    ret_0 = head + re_max # move some item to the head

    ret_1 = min_subarray(P, N-K) # only delete

    # we need to consider both situation
    # 6 5
    # 2 1 3 4 5 6
    ret = min(ret_1, ret_0)
    print(*ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)