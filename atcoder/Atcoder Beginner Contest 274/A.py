'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/22 20:46       
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
    A, B = map(int, lines[0].split(" "))
    print(format(B/A, '.3f'))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)