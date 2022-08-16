'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 21:02       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    R, C = map(int, lines[0].split(" "))
    l, r = min(R, 16-R), max(R, 16-R)
    if C < l:
        if (R + l - C) % 2:
            print("black")
        else:
            print("white")
    elif C > r:
        if (R + r - C) % 2:
            print("black")
        else:
            print("white")
    else:
        if R % 2:
            print("black")
        else:
            print("white")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)