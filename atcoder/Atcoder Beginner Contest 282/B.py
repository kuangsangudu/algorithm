'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/17 21:02       
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
    N, M = map(int, lines[0].split(' '))
    S = lines[1:]
    target = (1 << M) - 1
    arr = []
    for s in S:
        re = 0
        for i, n in enumerate(s):
            if n == "o":
                re += 1 << i
        arr.append(re)

    ret = 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] | arr[j] == target:
                ret += 1
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)