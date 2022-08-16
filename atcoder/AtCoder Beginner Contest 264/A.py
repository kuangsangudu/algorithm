'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 20:06       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    L, R = map(int, lines[0].split(" "))
    print("atcoder"[L-1:R])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)