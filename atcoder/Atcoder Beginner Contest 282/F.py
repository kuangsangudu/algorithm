'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/18 10:55       
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


def main():
    N = int(input())
    tree = [[], []]
    arr = []
    idx = 1
    for i in range(1, N + 1):
        j = i
        start = 1
        while j <= N:
            arr.append([i, j])
            tree[-1].append(idx)
            idx += 1
            start *= 2
            j = i + start - 1
        tree.append([])

    print(len(arr), flush=True)
    for a in arr:
        print(*a, flush=True)

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        mid = int(math.log2(r-l+1))
        print(tree[l][mid], tree[r - (1 << mid)+1][mid], flush=True)


if __name__ == '__main__':
    main()


