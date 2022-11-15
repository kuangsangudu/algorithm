'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 21:20       
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
    N, M = map(int, lines[0].split(' '))
    A = list(map(int, lines[1].split(" ")))
    count = collections.Counter(A)
    a = sum(A)
    ret = 0
    sums = 0
    keys = sorted(count.keys()) * 2

    for i, key in enumerate(keys):
        if i > 0 and key == (keys[i-1]+1) % M:
            sums += count[key] * key
        else:
            sums = count[key] * key
        ret = max(ret, sums)

    if ret >= a:
        print(0)
    else:
        print(a-ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)