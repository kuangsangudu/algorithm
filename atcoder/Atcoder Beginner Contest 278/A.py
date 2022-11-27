'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 20:53       
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


def main(lines):
    N, K = map(int, lines[0].split(' '))
    A = list(map(int, lines[1].split(" ")))
    if K >= len(A):
        print(*([0] * len(A)))
    else:
        print(*(A[K:] + [0] * K))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
