'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 20:55       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    print(sum(A))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)