'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 21:37       
@Author:ZHANG               
 
'''
import collections
import sys


def DFS(graph, s, N):
    stack = [s]
    seen = set()
    parent = [-1] * (N+1)
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex in seen:
            continue
        if vertex != s:
            print("{} {}".format(vertex, parent[vertex]))
        seen.add(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                parent[w] = vertex
                stack.append(w)


def BFS(graph, s):
    queue = collections.deque([s])
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.popleft()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                print("{} {}".format(vertex, w))
                queue.append(w)
                seen.add(w)


def main(lines):
    N, M = list(map(int, lines[0].split(" ")))
    graph = collections.defaultdict(list)
    for line in lines[1:]:
        u, v = list(map(int, line.split(" ")))
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    # def dfs(n):
    #     if n in visited:
    #         return
    #     visited.add(n)
    #     for nxt in graph[n]:
    #         if nxt not in visited:
    #             print(n + " " + nxt)
    #             dfs(nxt)
    # dfs("1")
    DFS(graph, 1, N)
    BFS(graph, 1)
    # Q = collections.deque(["1"])
    # while Q:
    #     i = Q.popleft()
    #     visited.add(i)
    #     for nxt in graph[i]:
    #         if nxt not in visited:
    #             visited.add(nxt)
    #             print(i + " " + nxt)
    #             Q.append(nxt)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
