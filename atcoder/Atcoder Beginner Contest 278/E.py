'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/19 21:48       
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
    H, W, N, h, w = map(int, lines[0].split(" "))
    A = []
    maps = collections.Counter()
    for line in lines[1:]:
        A.append(list(map(int, line.split(" "))))
        maps.update(collections.Counter(A[-1]))

    ret = []
    flag = False
    for i in range(H-h+1):
        if not flag:
            flag = True
            for m in range(h):
                for n in range(w):
                    maps[A[m][n]] -= 1
                    if maps[A[m][n]] == 0:
                        maps.pop(A[m][n])
        elif i % 2 == 0:
            for j in range(w):
                maps[A[i-1][j]] += 1
                maps[A[i+h-1][j]] -= 1
                if maps[A[i+h-1][j]] == 0:
                    maps.pop(A[i+h-1][j])
        else:
            for j in range(w):
                maps[A[i-1][W-j-1]] += 1
                maps[A[i+h-1][W-j-1]] -= 1
                if maps[A[i+h-1][W-j-1]] == 0:
                    maps.pop(A[i+h-1][W-j-1])

        ret.append([len(maps)])

        if i % 2 == 0:
            for j in range(1, W-w+1):
                for n in range(i, i+h):
                    maps[A[n][j-1]] += 1
                    maps[A[n][j+w-1]] -= 1
                    if maps[A[n][j+w-1]] == 0:
                        maps.pop(A[n][j+w-1])
                ret[-1].append(len(maps))
        else:
            for j in range(W-2, w-2, -1):
                for n in range(i, i+h):
                    maps[A[n][j+1]] += 1
                    maps[A[n][j-w+1]] -= 1
                    if maps[A[n][j-w+1]] == 0:
                        maps.pop(A[n][j-w+1])
                ret[-1].append(len(maps))
            ret[-1] = ret[-1][::-1]

    for r in ret:
        print(*r)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
