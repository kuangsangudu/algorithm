'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/04 19:09       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N, k = map(int, lines[0].split(" "))
    arr = sorted(lines[1:k+1])
    print(*arr, sep="\n")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)