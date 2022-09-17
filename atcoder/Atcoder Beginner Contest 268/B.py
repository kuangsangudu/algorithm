'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 21:02       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    a = lines[0]
    b = lines[1]
    if a == b[:len(a)]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)