'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/11 0:19       
@Author:ZHANG               
 
'''
'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 21:28       
@Author:ZHANG               

'''
import collections
import itertools
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    S = lines[1:]
    T = []
    for i, s in enumerate(S):
        digit = 0
        xnums = 0
        for j in s:
            if j.isdigit():
                digit += int(j)
            else:
                xnums += 1
        T.append([digit, xnums, s])

    eps = 10**-5
    S = sorted(T, key=lambda x: x[0]/(x[1]+eps))
    ret = 0
    sums = 0
    for n in S:
        for i in n[2]:
            if i.isdigit():
                ret += sums * int(i)
            else:
                sums += 1
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)