'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 21:02       
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
    maps = collections.defaultdict(dict)
    one = "HDCS"
    two = "A23456789TJQK"
    for s in lines[1:]:
        first, second = s[0], s[1]
        if first in one and second in two and maps[first].get(second, -1) == -1:
            maps[first][second] = 1
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)