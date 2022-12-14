'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 21:40       
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
from sortedcontainers import SortedList


def main(lines):
    N, M, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))

    arr = SortedList(A[:M])
    ret = [sum(arr[:K])]
    sums = ret[0]
    right = K
    for i in range(1, N-M+1):
        idx = arr.bisect(A[i-1])
        arr.remove(A[i-1])
        if idx <= right:
            sums -= A[i-1]
            if K > 1:
                sums += arr[K-1]

        arr.add(A[i + M - 1])
        if arr.bisect(A[i + M - 1]) <= right:
            if K > 1:
                sums -= arr[K]
            sums += A[i+M-1]
        ret.append(sums)

    print(*ret)


def main1(lines):
    N, M, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))

    l, r = [], []
    del_l, del_r = [], []
    arr = sorted(A[:M])
    for i in range(M):
        if i < K:
            heapq.heappush(l, -arr[i])
        else:
            heapq.heappush(r, arr[i])

    inf = float("inf")
    heapq.heappush(r, inf)
    ret = [-sum(l)]
    sums = ret[0]
    for i in range(1, N-M+1):
        if A[i-1] < r[0]:
            heapq.heappush(del_l, -A[i-1])
            sums -= A[i-1]

            while r and del_r and r[0] == del_r[0]:
                heapq.heappop(r)
                heapq.heappop(del_r)

            if r[0] != inf:
                sums += r[0]
                heapq.heappush(l, -heapq.heappop(r))
        else:
            heapq.heappush(del_r, A[i-1])

        if A[i+M-1] < r[0]:
            while l and del_l and l[0] == del_l[0]:
                heapq.heappop(l)
                heapq.heappop(del_l)

            heapq.heappush(l, -A[i+M-1])
            sums += A[i+M-1]

            if len(l) > K:
                sums += l[0]
                heapq.heappush(r, -heapq.heappop(l))
        else:
            heapq.heappush(r, A[i+M-1])

        ret.append(sums)

    print(*ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)
