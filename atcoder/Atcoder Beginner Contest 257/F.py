'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/26 1:06       
@Author:ZHANG               
 
'''
import collections
import sys


def Bfs(graph, sp, N):
    ret = [float("inf")] * (N+1)
    ret[sp] = 0
    Q = collections.deque([[sp, 0]])
    while Q:
        p, dis = Q.popleft()
        if ret[p] < dis:
            continue
        for nxt in graph[p]:
            if ret[nxt] > dis+1:
                Q.append([nxt, dis+1])
                ret[nxt] = dis+1
    return ret


def main(lines):
    N, M = map(int, lines[0].split(" "))
    graph = collections.defaultdict(list)
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        graph[u].append(v)
        graph[v].append(u)

    bfs1 = Bfs(graph, 1, N)
    bfs0 = Bfs(graph, 0, N)
    bfsN = Bfs(graph, N, N)
    ret = [str(-1)] * N
    for i in range(1, N+1):
        if i == 1:
            re = min(bfs1[N], bfs0[N])
        elif i == N:
            re = min(bfs1[N], bfs1[0])
        else:
            re = min(bfs1[N], bfsN[0]+bfs1[0], bfsN[i]+bfs1[0], bfsN[0]+bfs1[i])
        if re != float("inf"):
            ret[i-1] = str(re)
    print(" ".join(ret))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
