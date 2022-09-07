'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 21:53       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, M = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    maps = collections.defaultdict(list)
    for line in lines[2:]:
        u, v = map(int, line.split(" "))
        maps[u].append(v)
        maps[v].append(u)

    visited = set()
    q = []
    re = collections.defaultdict(int)
    for key, val in maps.items():
        sums = 0
        for i in val:
            sums += A[i-1]
        heapq.heappush(q, [sums, key])
        re[key] = sums

    ret = 0
    while len(q) and len(visited) < N:
        s, key = heapq.heappop(q)
        if key in visited:
            continue
        ret = max(ret, s)
        visited.add(key)
        for nxt in maps[key]:
            if nxt not in visited:
                re[nxt] -= A[key-1]
                heapq.heappush(q, [re[nxt], nxt])
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)