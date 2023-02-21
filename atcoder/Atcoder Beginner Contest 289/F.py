'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/17 12:12       
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
    def move(x, y, m, n):
        x = 2 * m - x
        y = 2 * n - y
        ret.append([m, n])
        return x, y

    sx, sy = map(int, lines[0].split(" "))
    tx, ty = map(int, lines[1].split(" "))
    a, b, c, d = map(int, lines[2].split(" "))

    ret = []
    if sx % 2 != tx % 2 or sy % 2 != ty % 2:
        print("No")
        return
    if a == b and sx != tx:
        sx, sy = move(sx, sy, a, c)
    if c == d and sy != ty:
        sx, sy = move(sx, sy, a, c)
    if (a == b and sx != tx) or (c == d and sy != ty):
        print("No")
        return

    while sx < tx:
        sx, sy = move(sx, sy, a, c)
        sx, sy = move(sx, sy, a+1, c)
    while sx > tx:
        sx, sy = move(sx, sy, a + 1, c)
        sx, sy = move(sx, sy, a, c)
    while sy < ty:
        sx, sy = move(sx, sy, a, c)
        sx, sy = move(sx, sy, a, c+1)
    while sy > ty:
        sx, sy = move(sx, sy, a, c+1)
        sx, sy = move(sx, sy, a, c)
    if sx != tx or sy != ty:
        print("No")
    else:
        print("Yes")
        for arr in ret:
            print(*arr)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)