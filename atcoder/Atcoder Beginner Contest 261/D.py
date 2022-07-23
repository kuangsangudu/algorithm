'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 21:21       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, M = map(int, lines[0].split(" "))
    X = list(map(int, lines[1].split(" ")))
    C = {}
    for line in lines[2:]:
        c1, y1 = map(int, line.split(' '))
        C[c1] = y1
    dp = collections.defaultdict(int)
    dp[0] = 0
    for i in range(N):
        ndp = collections.defaultdict(int)
        for key, val in dp.items():
            ndp[key+1] = max(ndp[key+1], val+X[i]+C.get(key+1, 0))
            ndp[0] = max(ndp[0], val)
        dp = ndp
    print(max(dp.values()))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)