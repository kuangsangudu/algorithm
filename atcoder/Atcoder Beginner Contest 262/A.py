'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/31 21:02       
@Author:ZHANG               
 
'''
import math
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


def main(lines):
    y = int(lines[0])
    x = math.ceil((y-2)/4)
    print(4 * x + 2)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
