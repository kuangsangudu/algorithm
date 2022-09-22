'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 21:01       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    S = lines
    a = []
    for i, row in enumerate(lines):
        for j, n in enumerate(row):
            if n == "#":
                a = [i, j]
                break
        if a:
            break

    b = []
    for i in range(len(lines)-1, -1, -1):
        for j in range(len(lines[0])-1, -1, -1):
            if lines[i][j] == "#":
                b = [i, j]
                break
        if b:
            break
    print(a[0]+1, b[0]+1)
    print(a[1]+1, b[1]+1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)