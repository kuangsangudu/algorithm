'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/29 20:40       
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
    N = int(lines[0])
    H = list(map(int, lines[1].split(" ")))
    maxh = max(H)
    print(H.index(maxh)+1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)