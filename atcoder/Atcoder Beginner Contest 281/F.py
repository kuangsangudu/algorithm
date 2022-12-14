'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 22:31       
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
    a = list(map(int, lines[1].split(" ")))

    def dfs(arr, idx):
        if idx < 0:
            return 0

        l, r = [], []
        for n in arr:
            if (n >> idx) & 1:
                l.append(n)
            else:
                r.append(n)

        if l and r:
            return min(dfs(l, idx-1), dfs(r, idx-1)) | (1 << idx)
        elif l:
            return dfs(l, idx-1)
        else:
            return dfs(r, idx-1)

    print(dfs(a, 29))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
