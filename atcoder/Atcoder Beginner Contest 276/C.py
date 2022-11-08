'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 11:10
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
    p = list(map(int, lines[1].split(" ")))
    for i in range(len(p)-1, -1, -1):
        if p[i] < p[i-1]:
            start = i
            for j in range(len(p)-1, i, -1):
                if p[start] < p[j] < p[i-1]:
                    start = j
            p[i-1], p[start] = p[start], p[i-1]
            p = p[:i] + sorted(p[i:], reverse=True)
            break
    print(*p)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)