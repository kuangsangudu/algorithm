'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/20 20:53       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
import itertools
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    A.sort()
    ans = sorted([str(A[-1]), str(A[-2]), str(A[-3])], reverse=True)
    print("".join(ans))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)