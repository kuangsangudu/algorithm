'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/27 21:07       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    lines = [list(map(int, line.split(" ")))for line in lines]
    ans = 'Yes'
    for i in range(4):
        x0, y0 = lines[i]
        x1, y1 = lines[(i + 1) % 4]
        x2, y2 = lines[(i - 1) % 4]

        v1 = [x1 - x0, y1 - y0]
        v2 = [x2 - x0, y2 - y0]

        s = v1[0] * v2[1] - v1[1] * v2[0]
        if s <= 0:
            ans = 'No'
            break

    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)