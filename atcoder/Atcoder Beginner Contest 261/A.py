'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 20:06       
@Author:ZHANG               
 
'''
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    L1, R1, L2, R2 = map(int, lines[0].split(" "))
    if L2 > R1 or L1 > R2:
        print(0)
    else:
        print(min(R2, R1)-max(L2, L1))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)