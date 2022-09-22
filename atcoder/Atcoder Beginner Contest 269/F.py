'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/17 22:01       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def left_down(x, y, odd):
    lx = x if x % 2 == odd else x+1
    ly = y if (lx+y) % 2 == 0 else y+1
    return lx, ly


def right_up(x, y, odd):
    rx = x if x % 2 == odd else x-1
    ry = y if (rx+y) % 2 == 0 else y-1
    return rx, ry


def get_num(i, j, M):
    return (i-1) * M + j


# using the Arithmetic Array Summation to solve the problem
def sums(lx, rx, ly, ry, odd, M):
    lx_odd, ly_odd = left_down(lx, ly, odd)
    rx_odd, ry_odd = right_up(rx, ry, odd)
    ret = 0
    if lx_odd <= rx_odd and ly_odd <= ry_odd:
        nums = math.ceil((rx_odd + 1 - lx_odd) / 2)
        first = (get_num(lx_odd, ly_odd, M) + get_num(rx_odd, ly_odd, M)) * nums // 2
        ret = (first + first + (ry_odd - ly_odd) * nums) * math.ceil((ry_odd + 1 - ly_odd) / 2) // 2
    return ret


def main(lines):
    N, M = map(int, lines[0].split(" "))
    mod = 998244353
    for line in lines[2:]:
        lx, rx, ly, ry = map(int, line.split(" "))
        print((sums(lx, rx, ly, ry, 0, M) + sums(lx, rx, ly, ry, 1, M)) % mod)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)