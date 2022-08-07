'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 21:10       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def xunzhao(N, M, start, i):
    ret = []
    for nxt in range(start+1, M+1):
        if i + 1 < N:
            re = xunzhao(N, M, nxt, i+1)
            for j in range(len(re)):
                ret.append([start] + re[j])
        else:
            ret.append([start, nxt])
    return ret


def main(lines):
    N, M = map(int, lines[0].split(" "))
    for i in range(1, M+1):
        if N > 1:
            ret = xunzhao(N, M, i, 1)
            for r in ret:
                print(*r)
        else:
            print(i)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)