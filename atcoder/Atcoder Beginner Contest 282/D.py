'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/17 21:13       
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
    graph = [[] for _ in range(1+N)]
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (N+1)

    def dfs(i, color):
        colors[i] = color
        for nxt in graph[i]:
            if colors[nxt] == 0:
                colors[nxt] = -color
                if not dfs(nxt, -color):
                    return False
            elif colors[nxt] == colors[i]:
                return False
        return True

    start = 1
    for i in range(1, N+1):
        if colors[i] == 0:
            q = collections.deque([i])
            colors[i] = start
            while q:
                node = q.popleft()
                cNei = -colors[node]
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        q.append(neighbor)
                        colors[neighbor] = cNei
                    elif colors[neighbor] != cNei:
                        print(0)
                        return
            start += 1

    ret = 0
    counts = collections.Counter(colors[1:])
    for i in range(1, N+1):
        ret += N-counts[colors[i]]-len(graph[i])
    print(ret//2)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)