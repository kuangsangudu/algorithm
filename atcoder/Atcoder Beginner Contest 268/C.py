'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 21:04       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    P = list(map(int, lines[1].split(" ")))
    maps = collections.defaultdict(int)
    for i, p in enumerate(P):
        maps[(p - i) % N] += 1
        maps[(p - i + 1) % N] += 1
        maps[(p - i - 1) % N] += 1
    print(max(maps.values()))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)