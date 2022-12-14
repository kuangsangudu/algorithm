'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 20:52       
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


def main(lines):
    N = int(lines[0])
    for i in range(N, -1, -1):
        print(i)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
