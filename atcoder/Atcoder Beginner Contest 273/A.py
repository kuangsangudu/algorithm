'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 20:21       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def f(i):
    if i <= 0:
        return 1
    return i * f(i-1)


def main(lines):
    print(f(int(lines[0])))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)