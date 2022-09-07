'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 21:24       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, M = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    sums = [0] * (len(A)+1)
    for i, n in enumerate(A):
        sums[i+1] = sums[i] + n
    re = 0
    for i in range(M):
        re += (i+1) * A[i]
    ret = re
    for i in range(1, N-M+1):
        re = re - (sums[i-1+M]-sums[i-1]) + M * A[i+M-1]
        ret = max(re, ret)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)