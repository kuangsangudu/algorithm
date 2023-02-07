'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/04 18:40       
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

sys.setrecursionlimit(10**6)


def main(lines):
    N = int(lines[0])
    for line in lines[1:]:
        print(sum(map(int, line.split(" "))))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)