'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 22:14       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    graph = [[] for _ in range(N+1)]
    for line in lines[1:N]:
        u, v = map(int, line.split(" "))
        graph[u].append(v)
        graph[v].append(u)

    # get the depth list of the tree when the root is at root
    def dfs(root):
        depth = [-1] * (N+1)
        depth[root] = 0
        q = [root]
        while q:
            v = q.pop()
            for nxt in graph[v]:
                if depth[nxt] == -1:
                    q.append(nxt)
                    depth[nxt] = depth[v] + 1
        return depth

    depth1 = dfs(1)
    root1 = max(range(1, N+1), key=lambda x: depth1[x])
    depth2 = dfs(root1)
    root2 = max(range(1, N+1), key=lambda x: depth2[x])

    Q = int(lines[N])
    ret = [-1] * Q
    queries = [[] for _ in range(N+1)]
    for i, line in enumerate(lines[N + 1:]):
        u, k = map(int, line.split(" "))
        queries[u].append([k, i])

    def level_ancestor(root):
        g = [len(graph[i]) for i in range(len(graph))]
        q = [-1, root]
        while len(q) != 1:
            if g[q[-1]]:
                g[q[-1]] -= 1
                if graph[q[-1]][g[q[-1]]] != q[-2]:
                    q.append(graph[q[-1]][g[q[-1]]])
            else:
                v = q.pop()
                for k, i in queries[v]:
                    if k < len(q):
                        ret[i] = q[-k]

    level_ancestor(root1)
    level_ancestor(root2)

    print(*ret, sep='\n')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
