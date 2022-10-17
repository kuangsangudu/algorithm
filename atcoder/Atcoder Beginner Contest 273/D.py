'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 21:25       
@Author:ZHANG               
 
'''
import bisect
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    H, W, x0, y0 = map(int, lines[0].split(" "))
    N = int(lines[1])

    wall_x = collections.defaultdict(list)
    wall_y = collections.defaultdict(list)
    for line in lines[2: N+2]:
        x, y = map(int, line.split(" "))
        wall_x[x].append(y)
        wall_y[y].append(x)
    for key in wall_x.keys():
        wall_x[key].sort()
    for key in wall_y.keys():
        wall_y[key].sort()

    Q = int(lines[N+2])
    for line in lines[N+3:]:
        d, l = line.split(" ")
        l = int(l)
        if d == "L":
            idx = bisect.bisect_left(wall_x[x0], y0)
            if idx == len(wall_x[x0]) or wall_x[x0][idx] > y0:
                idx -= 1
            if idx < 0 or y0 - wall_x[x0][idx] > l:
                x0, y0 = x0, max(1, y0-l)
            else:
                x0, y0 = x0, wall_x[x0][idx] + 1
        elif d == "R":
            idx = bisect.bisect_left(wall_x[x0], y0)
            if idx == len(wall_x[x0]) or -y0 + wall_x[x0][idx] > l:
                x0, y0 = x0, min(W, y0+l)
            else:
                x0, y0 = x0, wall_x[x0][idx] - 1
        elif d == "U":
            idx = bisect.bisect_left(wall_y[y0], x0)
            if idx == len(wall_y[y0]) or wall_y[y0][idx] > x0:
                idx -= 1
            if idx < 0 or x0 - wall_y[y0][idx] > l:
                x0, y0 = max(1, x0-l), y0
            else:
                x0, y0 = wall_y[y0][idx]+1, y0
        else:
            idx = bisect.bisect_left(wall_y[y0], x0)
            if idx == len(wall_y[y0]) or -x0 + wall_y[y0][idx] > l:
                x0, y0 = min(H, x0+l), y0
            else:
                x0, y0 = wall_y[y0][idx]-1, y0
        print(x0, y0)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

