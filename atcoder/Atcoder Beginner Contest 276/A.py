'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 0:22       
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
    for i in range(len(s)-1, -1, -1):
        if s[i] == "a":
            print(i+1)
            return
    print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)