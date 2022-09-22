'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 21:35       
@Author:ZHANG               
 
'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools
import math


def main():
    N = int(input())
    l, r = 1, N
    while l < r:
        mid = (l+r)//2
        print("? %d %d %d %d" % (l, mid, 1, N))
        n = int(input())
        if n == mid - l + 1:
            l = mid + 1
        else:
            r = mid
    x = l

    l, r = 1, N
    while l < r:
        mid = (l+r)//2
        print("? %d %d %d %d" % (1, N, l, mid))
        n = int(input())
        if n == mid - l + 1:
            l = mid + 1
        else:
            r = mid
    y = l
    print("! %d %d" % (x, y))


if __name__ == '__main__':
    main()