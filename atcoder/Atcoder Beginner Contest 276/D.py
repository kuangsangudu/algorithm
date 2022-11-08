'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 11:53       
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
import functools


def main(lines):
    n = int(lines[0])
    a = list(map(int, lines[1].split(" ")))

    def dfs(i) -> list:
        if i % 2 == 0:
            ret = dfs(i//2)
            ret[1] += 1
            return ret
        elif i % 3 == 0:
            ret = dfs(i//3)
            ret[2] += 1
            return ret
        return [i, 0, 0]

    re = []
    for n in a:
        re.append(dfs(n))

    min_2, min_3 = re[0][1], re[0][2]
    pre = re[0][0]
    sums = 0
    for n in re:
        if n[0] != pre:
            print(-1)
            return
        min_2 = min(n[1], min_2)
        min_3 = min(n[2], min_3)
        sums += n[1] + n[2]
    print(sums - (min_2+min_3) * len(re))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)