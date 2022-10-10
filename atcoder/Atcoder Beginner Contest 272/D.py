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
    direction = set()
    for i in range(M+1):
        if i ** 2 > M:
            break
        ano = int((M - i**2) ** 0.5)
        if ano ** 2 + i ** 2 == M:
            direction.add((i, ano))
            direction.add((i, -ano))
            direction.add((-i, ano))
            direction.add((-i, -ano))
            direction.add((ano, i))
            direction.add((-ano, i))
            direction.add((ano, -i))
            direction.add((-ano, -i))

    ret = [[-1] * N for _ in range(N)]
    ret[0][0] = 0
    q = collections.deque([[0, 0, 0]])
    while q:
        s, i, j = q.popleft()
        for dir in direction:
            nxti, nxtj = i+dir[0], j+dir[1]
            if 0 <= nxti < N and 0 <= nxtj < N and (ret[nxti][nxtj] == -1 or s+1 < ret[nxti][nxtj]):
                ret[nxti][nxtj] = s + 1
                q.append([s+1, nxti, nxtj])

    for row in ret:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)