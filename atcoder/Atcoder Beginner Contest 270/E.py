'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/24 22:12       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


def main(lines):
    def f(num):
        ret = 0
        for n in a:
            ret += min(num, n)
        return ret

    N, K = map(int, lines[0].split(" "))
    a = list(map(int, lines[1].split(" ")))
    l, r = 0, K
    while l < r:
        mid = l + (r-l+1)//2
        if f(mid) <= K:
            l = mid
        else:
            r = mid - 1

    # calculate the remaining apples and minus them
    last_k = K - f(l)
    for i in range(len(a)):
        if last_k and a[i] >= l+1:
            a[i] = max(0, a[i]-l-1)
            last_k -= 1
        else:
            a[i] = max(0, a[i]-l)
    print(*a)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)