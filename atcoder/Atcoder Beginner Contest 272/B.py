'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 21:01       
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
    N, M = map(int, lines[0].split(" "))
    ret = collections.defaultdict(set)
    visited = set()
    for i, line in enumerate(lines[1:]):
        line = list(map(int, line.split(" ")))
        for n in line[1:]:
            ret[n].add(i)

    for i, j in itertools.combinations(range(1, N+1), 2):
        if not(ret[i] & ret[j]):
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)