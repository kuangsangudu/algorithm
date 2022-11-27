'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 21:28       
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
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    maps = collections.defaultdict(list)
    for i, n in enumerate(A, start=1):
        maps[i] = [n, -1]
    pre = 0
    pre_idx = -1
    for i, line in enumerate(lines[3:]):
        q = list(map(int, line.split(" ")))
        if q[0] == 1:
            pre = q[1]
            pre_idx = i
        elif q[0] == 2:
            if maps[q[1]][1] >= pre_idx:
                maps[q[1]][0] += q[2]
            else:
                maps[q[1]][0] = pre + q[2]
            maps[q[1]][1] = i
        else:
            if maps[q[1]][1] >= pre_idx:
                print(maps[q[1]][0])
            else:
                print(pre)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
