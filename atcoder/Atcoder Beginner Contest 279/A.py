'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 20:50       
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
    s = lines[0]
    print(s.count("v") + s.count("w") * 2)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
