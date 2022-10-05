'''
@Project: algorithm   
@Description: TODO          
@Time:2022/10/01 21:31       
@Author:ZHANG               
 
'''
import collections
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, S = map(int, lines[0].split(" "))
    a = []
    b = []
    for line in lines[1:]:
        a1, b1 = map(int, line.split(" "))
        a.append(a1)
        b.append(b1)
    dp = [0] * 10001
    last = [[-1] * 10001 for _ in range(len(a))]
    dp[a[0]] = 1
    last[0][a[0]] = 1
    dp[b[0]] = 1
    last[0][b[0]] = 0

    for i in range(1, len(a)):
        newdp = [0] * 10001
        for j, n in enumerate(dp):
            if n:
                newdp[j+a[i]] = 1
                last[i][j+a[i]] = 1
                newdp[j+b[i]] = 1
                last[i][j+b[i]] = 0
        dp = newdp

    if dp[S] == 1:
        print("Yes")
        ret = ""
        start = S
        for i in range(len(a)-1, -1, -1):
            if last[i][start] == 1:
                ret += "H"
                start -= a[i]
            else:
                ret += "T"
                start -= b[i]
        print(ret[::-1])
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)