'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 21:38       
@Author:ZHANG               
 
'''
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


@functools.lru_cache(None)
def Red(n, x, y):
    if n == 1:
        return 0
    return Red(n-1, x, y) + x * Blue(n, x, y)


@functools.lru_cache(None)
def Blue(n, x, y):
    if n == 1:
        return 1
    return Red(n-1, x, y) + y * Blue(n-1, x, y)


def main(lines):
    N, X, Y = map(int, lines[0].split(" "))
    print(Red(N, X, Y))


def main1(lines):
    N, X, Y = map(int, lines[0].split(" "))
    pre_r, pre_b = 0, 1
    for _ in range(2, N+1):
        now_b = pre_r + Y * pre_b
        now_r = pre_r + X * now_b
        pre_r = now_r
        pre_b = now_b
    print(pre_r)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)