'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 21:45       
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
    dp = [[float("-inf")] * (M+1) for _ in range(N+1)]
    for i, n in enumerate(A):
        dp[i][0] = 0
        for j in range(1, M+1):
            dp[i+1][j] = max(dp[i][j], dp[i][j-1] + j * n)
    print(dp[-1][-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)