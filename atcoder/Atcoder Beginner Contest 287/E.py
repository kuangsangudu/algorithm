'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 21:41       
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


def main(lines):
    N = int(lines[0])
    tree = {}
    for s in lines[1:]:
        a = tree
        for i, n in enumerate(s, start=1):
            if a.get(n, -1) == -1:
                a[n] = {}
            a = a[n]
            a["#"] = a.get("#", 0) + 1

    for s in lines[1:]:
        ret = 0
        a = tree
        for i, n in enumerate(s, start=1):
            a = a[n]
            if a["#"] > 1:
                ret = i
        print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)