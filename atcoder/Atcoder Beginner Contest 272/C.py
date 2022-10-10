'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 21:06       
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
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    A.sort(reverse=True)
    odd, odd_num = 0, 0
    even, even_num = 0, 0
    for n in A:
        if n % 2 and odd_num < 2:
            odd += n
            odd_num += 1
        elif n % 2 == 0 and even_num<2:
            even += n
            even_num += 1

    ret = -1
    if odd_num == 2:
        ret = max(ret, odd)
    if even_num == 2:
        ret = max(ret, even)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)