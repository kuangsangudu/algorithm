'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 21:04       
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

sys.setrecursionlimit(10 ** 9)


def main(lines):
    N, T = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    sums = sum(A)
    T %= sums

    acc = 0
    for i, n in enumerate(A, start=1):
        if acc + n < T:
            acc += n
        else:
            print(i, T-acc)
            break


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
