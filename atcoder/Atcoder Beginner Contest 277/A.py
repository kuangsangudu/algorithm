'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/12 20:52       
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
    N, X = map(int, lines[0].split(" "))
    P = list(map(int, lines[1].split(" ")))
    print(P.index(X)+1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)