'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 22:17       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    c = []
    for line in lines[1:]:
        c.append([0]+list(map(int, line.split(" "))))

    pre = collections.defaultdict(dict)
    allsums = pow(2, N)
    for i in range(allsums):
        pre[allsums+i][i] = 0

    for i in range(1, N+1):
        g = collections.defaultdict(dict)

        for j in range(allsums, allsums*2, 2):
            l_max = max(pre[j].values())
            r_max = max(pre[j+1].values())
            parent = j//2
            for k, v in pre[j].items():
                g[parent][k] = v+c[k][i]-c[k][i-1]+r_max
            for k, v in pre[j+1].items():
                g[parent][k] = v+c[k][i]-c[k][i-1]+l_max
        pre = g
        allsums //= 2

    print(max(pre[1].values()))


def main1(lines):
    n = int(lines[0])
    c = []
    for line in lines[1:]:
        c.append([0]+list(map(int, line.split(" "))))

    dp = [[0 for _ in range(1 << n)] for _ in range(n + 1)]
    for d in range(1, n + 1):
        for i in range(0, 1 << n, 1 << d):
            l = 0
            for j in range(i, i + (1 << (d - 1))):
                l = max(l, dp[d - 1][j] + c[j][d - 1])
            for j in range(i + (1 << (d - 1)), i + (1 << d)):
                dp[d][j] = dp[d - 1][j] + l

            r = 0
            for j in range(i + (1 << (d - 1)), i + (1 << d)):
                r = max(r, dp[d - 1][j] + c[j][d - 1])
            for j in range(i, i + (1 << (d - 1))):
                dp[d][j] = dp[d - 1][j] + r

    ans = 0
    for j in range(1 << n):
        ans = max(ans, dp[n][j] + c[j][n])
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)