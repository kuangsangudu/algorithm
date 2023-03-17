'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/21 12:41       
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
    T = int(lines[0])
    for line in lines[1:]:
        N, D, K = map(int, line.split(" "))
        D %= N
        n = N // math.gcd(N, D)
        K -= 1
        print((K % n) * D % N + K // n)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)