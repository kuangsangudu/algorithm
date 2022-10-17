'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 21:01       
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
    X, K = map(int, lines[0].split(" "))
    ret = X
    for i in range(1, K+1):
        ret = int(ret/(10**i)+0.5) * (10**i)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)