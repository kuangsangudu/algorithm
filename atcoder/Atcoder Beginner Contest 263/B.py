'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 21:03       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    p = list(map(int, lines[1].split(" ")))
    ret = [0] * N
    for i, n in enumerate(p):
        ret[i+1] = ret[n-1] + 1
    print(ret[-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)