'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/28 15:04       
@Author:ZHANG               
 
'''


# https://en.wikipedia.org/wiki/Suffix_array
# https://oi-wiki.org/string/sa/
#  sa[i] 表示将所有后缀排序后第 i 小的后缀的编号。 rk[i] 表示后缀 i 的排名。
import copy
from typing import List


# n2logn
def sample_id(s: str):
    sa = (len(s) + 1) * [0]
    rk = (len(s) + 1) * [0]
    arr = []
    for i in range(len(s)):
        arr.append([s[i:], i + 1])
    arr.sort()
    for i, (_, j) in enumerate(arr, start=1):
        rk[j] = i
        sa[i] = j
    return sa, rk


# nlog2n, it can use radix sort to reduce the time complexity to nlogn.
def suffix_array(s: str) -> (List[int], List[int]):
    n = len(s)
    sa = n * [0]
    rk = (n << 1) * [0]
    old_rk = (n << 1) * [0]
    for i in range(n):
        sa[i] = i
        rk[i] = ord(s[i])

    w = 1
    while w < n:
        # sa.sort(key=cmp_to_key(rk, w))
        sa.sort(key=lambda x: (rk[x], rk[x+w]))
        print(1, sa, rk)
        p = 1
        for i in range(n):
            if i == 0:
                old_rk[sa[i]] = p
                continue
            if rk[sa[i]] == rk[sa[i - 1]] and rk[sa[i] + w] == rk[sa[i - 1] + w]:
                old_rk[sa[i]] = p
            else:
                p += 1
                old_rk[sa[i]] = p
        rk, old_rk = old_rk, rk
        w <<= 1
    return sa, rk[:n]


def cmp_to_key(ra, w):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return ra[self.obj] < ra[other.obj] or (ra[self.obj] == ra[other.obj]
                                                        and ra[self.obj + w] < ra[other.obj + w])

        def __gt__(self, other):
            return ra[self.obj] > ra[other.obj] or (ra[self.obj] == ra[other.obj]
                                                        and ra[self.obj + w] > ra[other.obj + w])

        def __eq__(self, other):
            return ra[self.obj] == ra[other.obj] and ra[self.obj + w] == ra[other.obj + w]

        def __le__(self, other):
            return ra[self.obj] < ra[other.obj] or (ra[self.obj] == ra[other.obj]
                                                         and ra[self.obj + w] <= ra[other.obj + w])

        def __ge__(self, other):
            return ra[self.obj] > ra[other.obj] or (ra[self.obj] == ra[other.obj]
                                                         and ra[self.obj + w] >= ra[other.obj + w])

        def __ne__(self, other):
            return ra[self.obj] != ra[other.obj] and ra[self.obj+w] != ra[other.obj + w]

    return K


# nlogn method, sa[i] 表示将所有后缀排序后第 i 小的后缀的编号。 rk[i] 表示后缀 i 的排名。
def suffix2array(s: str) -> (List[int], List[int]):
    n = len(s)
    sa = n * [0]
    rk = (n << 1) * [0]
    key1 = n * [0]
    m = 127
    cnt = [0] * max(n, 127)
    for i in range(n):
        rk[i] = ord(s[i])
        cnt[rk[i]] += 1
    for i in range(1, m):
        cnt[i] += cnt[i - 1]
    for i in range(n - 1, -1, -1):
        cnt[rk[i]] -= 1
        sa[cnt[rk[i]]] = i

    old_rk = copy.deepcopy(rk)
    p = 0
    rk[sa[0]] = 0
    for i in range(1, n):
        if old_rk[sa[i]] == old_rk[sa[i - 1]]:
            rk[sa[i]] = p
        else:
            p += 1
            rk[sa[i]] = p

    w = 1
    while w < n:
        # 对第二关键字进行排序
        for i in range(n):
            cnt[i] = 0
        for i in range(n):
            key1[i] = sa[i]
        for i in range(n):
            cnt[rk[key1[i] + w]] += 1
        for i in range(1, n):
            cnt[i] += cnt[i - 1]
        for i in range(n - 1, -1, -1):
            cnt[rk[key1[i] + w]] -= 1
            sa[cnt[rk[key1[i] + w]]] = key1[i]

        # 对第一关键字，id[i]进行计数排序
        for i in range(n):
            cnt[i] = 0
        for i in range(n):
            key1[i] = sa[i]
        for i in range(n):
            cnt[rk[key1[i]]] += 1
        for i in range(1, n):
            cnt[i] += cnt[i - 1]
        for i in range(n - 1, -1, -1):
            cnt[rk[key1[i]]] -= 1
            sa[cnt[rk[key1[i]]]] = key1[i]

        p = 0
        for i in range(n):
            if i == 0:
                old_rk[sa[i]] = p
                continue
            if rk[sa[i]] == rk[sa[i - 1]] and rk[sa[i] + w] == rk[sa[i - 1] + w]:
                old_rk[sa[i]] = p
            else:
                p += 1
                old_rk[sa[i]] = p
        rk, old_rk = old_rk, rk
        w <<= 1
        if p == n:
            break
    return sa


if __name__ == '__main__':
    # s = "aabaaaab"
    # sa = [0, 1, 2, 3, 4, 5, 6, 7]
    # ra = [1, 1, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # sa = sorted(sa, key=lambda x: (ra[x], ra[x+1]))
    # print(sa)
    # newra = [0] * len(ra)
    # p = 1
    # w = 1
    # for i in range(8):
    #     if i == 0:
    #         newra[sa[i]] = p
    #         continue
    #     print(i, ra[sa[i]], ra[sa[i]+w], ra[sa[i-1]], ra[sa[i-1]+w])
    #     if ra[sa[i]] == ra[sa[i-1]] and ra[sa[i]+w] == ra[sa[i-1]+w]:
    #         newra[sa[i]] = p
    #     else:
    #         p += 1
    #         newra[sa[i]] = p
    # print(newra, ra)
    print(suffix2array("aabaaaab"))
    print(suffix_array("aabaaaab"))

    # sample_id(s)
