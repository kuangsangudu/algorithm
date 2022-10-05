'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 21:08       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    start = 1
    sort_a = sorted(set(a))
    remain = len(a) - len(sort_a)
    i = 0
    while remain or i < len(sort_a):
        if i < len(sort_a) and sort_a[i] == start:
            i += 1
            start += 1
        elif remain >= 2:
            remain -= 2
            start += 1
        else:
            while sort_a and remain < 2 and i < len(sort_a):
                sort_a.pop()
                remain += 1
            if remain >= 2:
                start += 1
                remain -= 2
            else:
                break
    print(start-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)