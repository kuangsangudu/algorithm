'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 22:03       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq
from typing import List
# from datastructure.string.Suffix_array.suffix_array import suffix2array

sys.setrecursionlimit(10 ** 9)
import functools
import copy


# https://atcoder.jp/contests/abc272/editorial/4988
# using suffix array to solve this problem, input is S * 2 + "a" * N + T * 2 + "z" * N

def main(lines):
    N = int(lines[0])
    S = lines[1]
    T = lines[2]
    # sa = suffix2array(T * 2 + "{" + S * 2)
    a = T * 2 + "{" + S * 2
    S = [ord(s) for s in a]
    sa = SA_IS(S)
    ret = 0
    len_t = N
    for i in sa:
        if 0 <= i < N:
            len_t -= 1
        elif 2 * N + 1 <= i < 3 * N + 1:
            ret += len_t
    print(ret)


def SA_IS(a):
    a += [0]
    k = max(a) + 1
    n = len(a)

    def induce_l(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 1)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not stype[j]):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_s(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 0)
        for i in range(n)[::-1]:
            j = sa[i] - 1
            if j >= 0 and stype[j]:
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j

    def get_buckets(a, k, start=0):
        bucket = [0] * k
        for item in a:
            bucket[item] += 1
        s = 0
        for i in range(k):
            s += bucket[i]
            bucket[i] = s - (bucket[i] if start else 0)
        return bucket

    def set_lms(a, n, k, default_order):
        bucket = get_buckets(a, k)
        sa = [-1] * n
        for i in default_order[::-1]:
            bucket[a[i]] -= 1
            sa[bucket[a[i]]] = i
        return sa

    def induce(a, n, k, stype, default_order):
        sa = set_lms(a, n, k, default_order)
        induce_l(sa, a, n, k, stype)
        induce_s(sa, a, n, k, stype)
        return sa

    def rename_LMS_substring(sa, a, n, stype, LMS, l):
        sa = [_s for _s in sa if LMS[_s]]
        tmp = [-1] * (n // 2) + [0]
        dupl = 0
        for _ in range(1, l):
            i, j = sa[_ - 1], sa[_]
            for ii in range(n):
                if a[i + ii] != a[j + ii] or stype[i + ii] != stype[j + ii]:
                    break
                if ii and (LMS[i + ii] or LMS[j + ii]):
                    dupl += 1
                    break
            tmp[j // 2] = _ - dupl
        tmp = [t for t in tmp if t >= 0]
        return tmp, dupl

    def calc(a, n, k):
        stype = [1] * n
        for i in range(n - 1)[::-1]:
            if a[i] > a[i + 1] or (a[i] == a[i + 1] and stype[i + 1] == 0):
                stype[i] = 0

        LMS = [1 if stype[i] and not stype[i - 1] else 0 for i in range(n - 1)] + [1]
        l = sum(LMS)
        lms = [i for i in range(n) if LMS[i]]
        sa = induce(a, n, k, stype, lms)
        renamed_LMS, dupl = rename_LMS_substring(sa, a, n, stype, LMS, l)

        if dupl:
            sub_sa = calc(renamed_LMS, l, l - dupl)
        else:
            sub_sa = [0] * l
            for i in range(l):
                sub_sa[renamed_LMS[i]] = i

        lms = [lms[sub_sa[i]] for i in range(l)]
        sa = induce(a, n, k, stype, lms)
        return sa

    sa = calc(a, n, k)
    return sa


def LCP(s, n, sa):
    lcp = [-1] * (n + 1)
    rank = [0] * (n + 1)
    for i in range(n + 1): rank[sa[i]] = i

    h = 0
    lcp[0] = 0
    for i in range(n):
        j = sa[rank[i] - 1]
        if h > 0: h -= 1
        while j + h < n and i + h < n and s[j + h] == s[i + h]:
            h += 1
        lcp[rank[i] - 1] = h
    return lcp


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
