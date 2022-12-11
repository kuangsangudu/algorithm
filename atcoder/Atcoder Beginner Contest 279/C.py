'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 21:05       
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
    H, W = map(int, lines[0].split(" "))
    S = collections.Counter(zip(*lines[1:H+1]))
    T = collections.Counter(zip(*lines[H+1:]))
    if S == T:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
