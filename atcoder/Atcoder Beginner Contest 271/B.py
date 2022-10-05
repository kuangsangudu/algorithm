'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 21:04       
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
    N, Q = map(int, lines[0].split(" "))
    a = []
    for line in lines[1:N+1]:
        a.append(line.split(" ")[1:])
    for line in lines[N+1:]:
        s, t = map(int, line.split(" "))
        print(a[s-1][t-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)