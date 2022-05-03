'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/28 15:04       
@Author:ZHANG               
 
'''


# https://en.wikipedia.org/wiki/Suffix_array
# https://oi-wiki.org/string/sa/
#  sa[i] 表示将所有后缀排序后第 i 小的后缀的编号。 rk[i] 表示后缀 i 的排名。


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
def suffix_array(s: str):
    n = len(s)
    sa = n * [0]
    rk = (n << 1) * [0]
    old_rk = (n << 1) * [0]
    for i in range(n):
        sa[i] = i
        rk[i] = ord(s[i])

    w = 1
    while w < n:
        sa.sort(key=cmp_to_key(rk, w))
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


if __name__ == '__main__':
    # s = "aabaaaab"
    # sa = [0, 1, 2, 3, 4, 5, 6, 7]
    # ra = [1, 1, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # sa = sorted(sa, key=cmp_to_key(ra, 1))
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
    print(suffix_array("aabaaaab"))

    # sample_id(s)
