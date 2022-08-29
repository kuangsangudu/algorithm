'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/26 11:23       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    print(lines[0][len(lines[0])//2])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
