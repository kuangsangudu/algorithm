'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 20:56       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    a, b, c, d = map(int, lines[0].split(" "))
    print((a+b)*(c-d))
    print("Takahashi")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)