'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/27 22:12       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    graph = collections.defaultdict(list)
    dis = collections.defaultdict(int)
    for i in range(1, N+1):
        u, v = map(int, lines[i].split(" "))
        graph[u].append(v)
        graph[v].append(u)
        dis[u] += 1
        dis[v] += 1

    # find the vertices than can be visited(not cycled)
    u = collections.deque([key for key, v in dis.items() if v == 1])
    visited = set()
    while u:
        idx = u.popleft()
        visited.add(idx)
        for nxt in graph[idx]:
            dis[nxt] -= 1
            if dis[nxt] == 1:
                u.append(nxt)

    # get cycles
    cycles = set(graph.keys()).difference(visited)
    par = collections.defaultdict(int)

    # get the ancestor of other vertices
    for c in cycles:
        u = collections.deque([c])
        while u:
            i = u.popleft()
            for nxt in graph[i]:
                if nxt not in cycles and not par[nxt]:
                    par[nxt] = c
                    u.append(nxt)

    for line in lines[N+2:]:
        u, v = map(int, line.split(" "))
        if (par[u] == par[v] and par[u]) or (par[u] == 0 and par[v] == u) or (par[v] == 0 and par[u] == v):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
