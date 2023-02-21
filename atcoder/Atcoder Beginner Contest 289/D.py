'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/14 16:08       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import functools
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    M = int(lines[2])
    B = set(map(int, lines[3].split(" ")))
    X = int(lines[4])
    inf = float("inf")
    dp = [inf] * (X+1)
    dp[0] = 0
    for i in range(X+1):
        if dp[i] != inf:
            for nxt in A:
                if i+nxt <= X and i+nxt not in B:
                    dp[i+nxt] = min(dp[i+nxt], dp[i]+1)

    if dp[-1] != inf:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)