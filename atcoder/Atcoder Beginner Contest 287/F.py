'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 22:00       
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

sys.setrecursionlimit(10**6)


def main(lines):
    mod = 998244353

    def dfs(u, p):
        dp0 = [1, 0]
        dp1 = [0, 1]
        for nxt in graph[u]:
            if nxt == p:
                continue
            r0, r1 = dfs(nxt, u)
            ndp0 = [0] * (len(dp0)+len(r0)-1)
            ndp1 = [0] * (len(dp1)+len(r1)-1)
            for i in range(len(dp0)):
                for j in range(1, len(r0)):
                    ndp0[i+j] += dp0[i] * (r0[j]+r1[j])
                    ndp0[i + j] %= mod
                    ndp1[i+j] += dp1[i] * r0[j]
                    ndp1[i + j] %= mod
                    ndp1[i+j-1] += dp1[i] * r1[j]
                    ndp1[i + j-1] %= mod

                # j == 0
                ndp0[i] += dp0[i] * (r0[0]+r1[0])
                ndp0[i] %= mod
                ndp1[i] += dp1[i] * r0[0]
                ndp1[i] %= mod

            dp0, dp1 = ndp0, ndp1
        return dp0, dp1

    N = int(lines[0])
    graph = [[] for _ in range(N)]
    for line in lines[1:]:
        a, b = map(int, line.split(" "))
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    r0, r1 = dfs(0, -1)
    for i in range(1, N+1):
        print((r0[i] + r1[i]) % mod)
    # print(*map(lambda p: sum(p) % mod, [*zip(*dfs(0, -1))][1:]), sep='\n')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

