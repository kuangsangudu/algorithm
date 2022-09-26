'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/24 21:11       
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
    N, X, Y = map(int, lines[0].split(" "))
    par = [-1] * (N+1)
    maps = collections.defaultdict(list)
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        maps[u].append(v)
        maps[v].append(u)
    q = collections.deque([X])
    par[X] = -2
    while q:
        i = q.popleft()
        if i == Y:
            break
        for nxt in maps[i]:
            if par[nxt] == -1:
                par[nxt] = i
                q.append(nxt)
    ret = []
    pre = Y
    while par[pre] != -2:
        ret.append(pre)
        pre = par[pre]
    ret.append(X)
    print(*ret[::-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)