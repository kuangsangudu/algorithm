'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 21:03       
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
import functools


def main(lines):
    H, M = map(int, lines[0].split(' '))
    h_one, h_ten = H % 10, H // 10
    for j in range(M, 60):
        if j//10 + h_ten * 10 <= 23 and h_one * 10 + j % 10 < 60:
            print(H, j)
            return

    for i in range(H+1, 24):
        h_one, h_ten = i % 10, i // 10
        for j in range(60):
            if j//10 + h_ten * 10 <= 23 and h_one * 10 + j % 10 < 60:
                print(i, j)
                return

    for i in range(H):
        h_one, h_ten = i % 10, i // 10
        for j in range(60):
            if j//10 + h_ten * 10 <= 23 and h_one * 10 + j % 10 < 60:
                print(i, j)
                return


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
