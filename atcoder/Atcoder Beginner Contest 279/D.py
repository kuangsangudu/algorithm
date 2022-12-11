'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 21:16       
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
    A, B = map(int, lines[0].split(" "))
    g = pow(2*B/A, -2/3)
    g_ceil = math.ceil(g)
    g_floor = int(g)
    print(min(A/pow(max(g_ceil, 1), 0.5)+max(0, (g_ceil-1))*B, A/pow(max(g_floor, 1), 0.5)+max(0, (g_floor-1))*B))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
