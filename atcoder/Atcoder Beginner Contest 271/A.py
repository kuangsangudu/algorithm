'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 20:47       
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
    ret = hex(int(lines[0]))[2:].upper()
    ret = ret if len(ret) == 2 else "0" + ret
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)