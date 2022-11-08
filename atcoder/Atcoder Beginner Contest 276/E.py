'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/05 12:12       
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
    H, W = map(int, lines[0].split(" "))
    maps = lines[1:]

    start = -1
    for i in range(H):
        for j in range(W):
            if maps[i][j] == "S":
                start = (i, j)

    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[0] * W for _ in range(H)]

    def bfs(m, n, target):
        q = collections.deque([(m, n)])
        while q:
            i, j = q.popleft()
            if (i, j) in target:
                return True
            for d in direction:
                ni, nj = i+d[0], j + d[1]
                if 0 <= ni < H and 0 <= nj < W and maps[ni][nj] != "#" and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
        return False

    s = {(start[0] - 1, start[1]), (start[0] + 1, start[1]), (start[0], start[1] + 1), (start[0], start[1] - 1)}
    visited[start[0]][start[1]] = 1
    for i, j in s:
        if 0 <= i < H and 0 <= j < W and maps[i][j] != "#":
            visited[i][j] = 1
            if bfs(i, j, s-{(i, j)}):
                print("Yes")
                return
            visited[i][j] = 0
    print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)