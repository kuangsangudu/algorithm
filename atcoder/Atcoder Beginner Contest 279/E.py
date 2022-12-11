'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 21:36       
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
    N, M = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))

    arr = list(range(1, N+1))
    pos = []
    for i, n in enumerate(A):
        pos.append([arr[n-1], arr[n]])
        arr[n-1], arr[n] = arr[n], arr[n-1]

    pos2idx = [0] * (N+1)
    for i, n in enumerate(arr):
        pos2idx[n] = i+1

    for i in range(M):
        if pos[i][0] == 1:
            print(pos2idx[pos[i][1]])
        elif pos[i][1] == 1:
            print(pos2idx[pos[i][0]])
        else:
            print(pos2idx[1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
