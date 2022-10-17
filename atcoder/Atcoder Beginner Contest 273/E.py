'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/15 22:05       
@Author:ZHANG               
 
'''

import bisect
import collections
import copy
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)
import functools


class Node:
    __slots__ = ("val", "par")

    def __init__(self, num, par=None):
        self.val = num
        self.par = par


def main(lines):
    Q = int(lines[0])
    maps = collections.defaultdict(Node)
    a = Node(-1)
    ret = [-1] * Q

    for i, line in enumerate(lines[1:]):
        if line == "DELETE":
            if a.val != -1:
                a = a.par
        else:
            act, n = line.split(" ")
            if act == "ADD":
                a = Node(n, par=a)
            elif act == "SAVE":
                maps[n] = a
            else:
                a = maps.get(n, Node(-1))

        ret[i] = a.val
    print(*ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

