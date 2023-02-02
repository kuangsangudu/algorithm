'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/16 11:32       
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


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    arr = [0] * N
    for i in range(1, N):
        arr[i] = arr[i-1] + A[(i-1)//2]

    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j]+arr[i-j-1])
    print(dp[-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)