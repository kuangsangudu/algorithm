'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/17 19:54       
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
    ret = ""
    for i in range(N):
        ret += chr(65 + i)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)