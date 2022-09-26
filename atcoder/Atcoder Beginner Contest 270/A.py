'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/24 20:04       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    A, B = map(int, lines[0].split(" "))
    print(A | B)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)