'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 21:28       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def f(n, m):
    q = [0] * n
    x = m
    while True:
        i = 0
        q[0] = x
        while True:
            yield q
            print("x: ", x)
            if i == 0:
                x = q[0] - 1
                i = 1
            elif q[0] == 0:
                x = q[i] - 1
                q[i] = 0
                i += 1

            if i >= n:
                return
            elif q[i] == m:
                print("zdy")
                x = x + m
                q[i] = 0
                i += 1
                if i >= n:
                    return

            q[i] += 1
            if x == 0:
                q[0] = 0
                continue
            else:
                break


def fun(c, sums, maps):
    ret = -1

    def f(i, sums, res):
        nonlocal ret
        if i == len(c)-1:
            res += c[i]
            if res not in maps and 16 >= len(res) >= 3:
                ret = res
            return

        for j in range(sums+1):
            if ret != -1:
                return
            f(i+1, sums-j, res + c[i] + "_" * (j+1))

    f(0, sums, "")
    return ret


def main(lines):
    N, M = map(int, lines[0].split(" "))
    S = lines[1:1+N]
    sums = 0
    for s in S:
        sums += len(s)
    sums = 16 - (N-1) - sums

    maps = {key: 1 for key in lines[1+N:]}
    for c in itertools.permutations(S):
        ret = fun(c, sums, maps)
        if ret != -1:
            print(ret)
            return
    print(-1)


# another solution
# def main(lines):
#     N, M = map(int, lines[0].split(" "))
#     S = lines[1:1 + N]
#     maps = {key: 1 for key in lines[1 + N:]}
#     if N == 1:
#         if S[0] not in maps and 3 <= len(S[0]) <= 16:
#             print(S[0])
#         else:
#             print(-1)
#         return
#     sums = 0
#     for s in S:
#         sums += len(s)
#     sums = 16 - (N - 1) - sums
#
#     for c in itertools.permutations(S):
#         s = "_".join(c)
#         if s not in maps and 3 <= len(s) <= 16:
#             print(s)
#             return
#         if sums > 0:
#             for ss in range(1, sums + 1):
#                 for q in f(N - 1, ss):
#                     s = ""
#                     for i, n in enumerate(q):
#                         s += c[i] + "_" * (n + 1)
#                     s += c[-1]
#                     if s not in maps and 3 <= len(s) <= 16:
#                         print(s)
#                         return
#     print(-1)


if __name__ == '__main__':
    # lines = []
    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))
    # main(lines)
    for n in f(2, 3):
        print(n[::-1])