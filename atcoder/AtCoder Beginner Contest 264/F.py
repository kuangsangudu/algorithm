'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 23:33       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    H, W = map(int, lines[0].split(" "))
    R = list(map(int, lines[1].split(" ")))
    C = list(map(int, lines[2].split(" ")))

    grid = [list(map(int, list(line))) for line in lines[3:]]

    inf = float("inf")
    # f[i][j][u][v] 在(i, j)这个格子，当前行操作了u次，当前列操作了v次
    f = [[[inf, inf], [inf, inf]] for _ in range(W)]
    f[0] = [[0, C[0]], [R[0], R[0] + C[0]]]

    for i in range(H):
        g = [[[inf, inf], [inf, inf]] for _ in range(W)]
        for j in range(W):
            for u in range(2):
                for v in range(2):
                    # down
                    if i + 1 < H:
                        a, b = grid[i][j] ^ u ^ v, grid[i + 1][j] ^ v
                        if a == b:
                            if g[j][0][v] > f[j][u][v]:
                                g[j][0][v] = f[j][u][v]
                        else:
                            if g[j][1][v] > f[j][u][v] + R[i + 1]:
                                g[j][1][v] = f[j][u][v] + R[i + 1]

                    # right
                    if j + 1 < W:
                        a, b = grid[i][j] ^ u ^ v, grid[i][j + 1] ^ u
                        if a == b:
                            if f[j + 1][u][0] > f[j][u][v]:
                                f[j + 1][u][0] = f[j][u][v]
                        else:
                            if f[j + 1][u][1] > f[j][u][v] + C[j + 1]:
                                f[j + 1][u][1] = f[j][u][v] + C[j + 1]

        if i == H-1:
            res = f[-1]
        f = g

    print(min(min(res[0]), min(res[1])))


def main1(lines):
    H, W = map(int, lines[0].split(" "))
    R = list(map(int, lines[1].split(" ")))
    C = list(map(int, lines[2].split(" ")))

    grid = [list(map(int, list(line))) for line in lines[3:]]

    inf = float("inf")
    f = [[inf] * 4 for _ in range(W)]
    f[0] = [0, R[0], C[0], C[0] + R[0]]

    for i in range(H):
        for j in range(W - 1):
            if grid[i][j] == grid[i][j + 1]:
                f[j + 1][0] = min(f[j + 1][0], f[j][0])
                f[j + 1][1] = min(f[j + 1][1], f[j][1])
                f[j + 1][2] = min(f[j + 1][2], f[j][2] + C[j + 1])
                f[j + 1][3] = min(f[j + 1][3], f[j][3] + C[j + 1])
            else:
                f[j + 1][0] = min(f[j + 1][0], f[j][2])
                f[j + 1][1] = min(f[j + 1][1], f[j][3])
                f[j + 1][2] = min(f[j + 1][2], f[j][0] + C[j + 1])
                f[j + 1][3] = min(f[j + 1][3], f[j][1] + C[j + 1])
        if i == H - 1:
            break

        c = R[i + 1]
        for j in range(W):
            if grid[i][j] == grid[i + 1][j]:
                f[j] = [f[j][0], f[j][1] + c, f[j][2], f[j][3] + c]
            else:
                f[j] = [f[j][1], f[j][0] + c, f[j][3], f[j][2] + c]

    # print(f[-1])
    print(min(f[-1]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)