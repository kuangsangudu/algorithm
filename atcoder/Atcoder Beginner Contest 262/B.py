'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 21:06       
@Author:ZHANG               
 
'''
import collections
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N, M = map(int, lines[0].split(" "))
    graph = collections.defaultdict(list)
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        graph[u].append(v)
        graph[v].append(u)
    ret = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for s in range(j+1, N+1):
                if j in graph[i] and j in graph[s] and i in graph[s]:
                    ret += 1
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)