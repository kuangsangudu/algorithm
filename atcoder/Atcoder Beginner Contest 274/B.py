'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/22 21:03       
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


def main(lines):
    H, W = map(int, lines[0].split(" "))
    c = lines[1:]
    ret = [0] * len(c[0])
    for i in range(len(c[0])):
        for j in range(len(c)):
            if c[j][i] == "#":
                ret[i] += 1
    print(*ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)