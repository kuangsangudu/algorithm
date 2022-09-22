'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 21:07       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    x = int(lines[0])
    ret = []
    start = x
    while start > 0:
        ret.append(start)
        start = (start-1) & x
    ret.append(0)
    ret = ret[::-1]

    for n in ret:
        print(n)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)