'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/27 21:31       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    lines = [list(map(int, line.split(" "))) for line in lines[1:]]
    dp = [float("-inf")] * 5
    dp[0] = 0
    idx = 0
    while idx < len(lines) and lines[0] == 0:
        dp[0] += lines[idx][2]
        idx += 1
    for i in range(1, lines[-1][0]+1):
        ndp = [0] * 5
        ndp[0] = max(dp[0], dp[1])
        ndp[1] = max(dp[0], dp[1], dp[2])
        ndp[2] = max(dp[3], dp[1], dp[2])
        ndp[3] = max(dp[4], dp[3], dp[2])
        ndp[4] = max(dp[3], dp[4])
        while idx < len(lines) and i == lines[idx][0]:
            ndp[lines[idx][1]] += lines[idx][2]
            idx += 1
        dp = ndp
    print(max(dp))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)