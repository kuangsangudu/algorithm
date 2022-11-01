'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/29 21:32       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


@functools.lru_cache(None)
def f(a):
    if a == 0:
        return 1
    return f(a//2) + f(a//3)


def main(lines):
    N = int(lines[0])
    print(f(N))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)