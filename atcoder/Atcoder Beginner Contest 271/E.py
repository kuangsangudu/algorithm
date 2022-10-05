'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 21:46       
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
    N, M, K = map(int, lines[0].split(" "))
    roads = []
    maps = collections.defaultdict(list)
    for line in lines[1:-1]:
        a, b, c = map(int, line.split(" "))
        roads.append([a, b, c])
        maps[a].append([b, c])
    mins = [float("inf")] * (N+1)
    mins[1] = 0
    E = list(map(int, lines[-1].split(" ")))
    for i in E:
        if mins[roads[i-1][0]] != float("inf"):
            mins[roads[i-1][1]] = min(mins[roads[i-1][1]], mins[roads[i-1][0]] + roads[i-1][2])

    if mins[N] != float("inf"):
        print(mins[N])
    else:
        print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)