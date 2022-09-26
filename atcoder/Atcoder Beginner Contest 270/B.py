'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/24 21:03       
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
    X, Y, Z = map(int, lines[0].split(" "))
    if X * Y >= 0 and Y * Z >= 0 and abs(Y) < abs(X) and abs(Y) < abs(Z):
        print(-1)
    elif abs(Y) > abs(X) or X * Y < 0:
        print(abs(X))
    else:
        print(abs(Z) + abs(X-Z))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)