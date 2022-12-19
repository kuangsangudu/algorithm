'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/17 21:08       
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
    N = int(lines[0])
    S = lines[1]
    ret = []
    sums = 0
    for s in S:
        if s == "\"":
            sums += 1
            ret.append("\"")
        elif s == ",":
            if sums % 2:
                ret.append(",")
            else:
                ret.append(".")
        else:
            ret.append(s)
    print("".join(ret))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)