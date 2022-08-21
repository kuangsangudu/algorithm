'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/20 21:14       
@Author:ZHANG               
 
'''
import collections
import copy
import sys
import heapq
import itertools
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, M, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))

    ret = 0
    count = 0
    for i in range(30, -1, -1):
        A.sort(reverse=True)
        new = []
        for j, n in enumerate(A):
            if n >> i & 1:
                new.append(0)
                A[j] -= 1 << i
            else:
                new.append((1 << i) - n)

        sums = sum(new[:K])
        if sums + count <= M:
            count += sums
            ret += 1 << i
            for j, n in enumerate(new):
                if n:
                    A[j] = 0
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)