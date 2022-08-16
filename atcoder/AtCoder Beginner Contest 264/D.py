'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 21:33       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
import itertools
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    s = list(lines[0])
    target = "atcoder"
    ret = 0
    for i in range(len(target)):
        if target[i] != s[0]:
            idx = s.index(target[i])
            ret += idx
            s.pop(idx)
        else:
            s.pop(0)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)