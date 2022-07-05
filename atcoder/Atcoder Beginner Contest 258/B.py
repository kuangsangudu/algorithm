'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/2 21:04       
@Author:ZHANG               
 
'''
import sys


def bfs(i, j, nums, N, direction):
    ret = ""
    for _ in range(N):
        ret += nums[i][j]
        i, j = (i + direction[0]) % N, (j + direction[1]) % N
    return int(ret)


def main(lines):
    N = int(lines[0])
    lines = lines[1:]
    maxs = "0"
    maxslist = []
    for i in range(N):
        for j in range(N):
            if lines[i][j] > maxs:
                maxs = lines[i][j]
                maxslist = [[i, j]]
            elif lines[i][j] == maxs:
                maxslist.append([i, j])

    dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    ret = 0
    for i, j in maxslist:
        for d in dir:
            ret = max(ret, bfs(i, j, lines, N, d))
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)