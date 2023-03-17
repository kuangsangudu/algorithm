'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/11 19:25       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import functools
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main(lines):
    s = [0] + list(lines[0])
    for i in range(1, len(s)//2+1):
        s[2*i], s[2*i-1] = s[2*i-1], s[2*i]
    print("".join(s[1:]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)