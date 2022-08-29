'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/27 22:10       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])

    def xunzhao(n):
        if n == N:
            return (1/6) * (1+2+3+4+5+6)
        nxt = xunzhao(n+1)
        ret = 0
        for i in range(1, 7):
            ret += (1/6) * max(i, nxt)
        return ret

    print(xunzhao(1))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)