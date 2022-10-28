'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/22 21:17       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def c(nums, t):
    maxs = max(nums) * len(nums)
    mins = -maxs
    if t > maxs or t < mins:
        return False

    dp = [False] * (maxs-mins+1)
    dp[-mins] = True
    for i in range(len(nums)):
        ndp = [False] * (maxs-mins+1)
        for j, n in enumerate(dp):
            if n:
                ndp[j+nums[i]] = True
                ndp[j-nums[i]] = True
        dp = ndp

    return dp[t-mins]


def main(lines):
    N, x, y = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    x_axis = []
    y_axis = []
    for i, n in enumerate(A):
        if i % 2:
            y_axis.append(n)
        else:
            x_axis.append(n)

    if c(x_axis[1:], x-x_axis[0]) and c(y_axis, y):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)