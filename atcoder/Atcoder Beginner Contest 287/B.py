'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 20:59       
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


def main(lines):
    N, M = map(int, lines[0].split(" "))
    S = lines[1: N+1]
    T = lines[N+1:]
    d = collections.Counter((s[3:]for s in S))
    ret = 0
    for num in T:
        if d.get(num, -1) != -1:
            ret += d[num]
            d.pop(num)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)