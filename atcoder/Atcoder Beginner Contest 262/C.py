'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 21:11       
@Author:ZHANG               
 
'''
import collections
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    same_idx = 0
    diff_idx = 0
    for i, n in enumerate(a):
        if n == i+1:
            same_idx += 1
        elif a[n-1] == i+1 and n > i+1:
            diff_idx += 1
    print(same_idx * (same_idx-1)//2 + diff_idx)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)