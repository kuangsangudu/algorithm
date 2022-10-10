'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 21:45       
@Author:ZHANG               
 
'''
'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/08 21:24       
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
    A = list(map(int, lines[1].split(" ")))
    c = collections.defaultdict(list)
    for i, n in enumerate(A, start=1):
        l = 1 if n >= 0 else min(M+1, math.ceil((-n)/i))
        r = min(M, math.ceil((M-n)/i))
        for j in range(l, r+1):
            c[j].append(n+i*j)

    for i in range(1, M+1):
        b = [False] * (len(c[i])+1)
        for num in c[i]:
            if num < len(c[i]):
                b[num] = True

        for j, n in enumerate(b):
            if not n:
                print(j)
                break


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)