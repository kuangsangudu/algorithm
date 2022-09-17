'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/10 20:02       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    print(len(set(map(int, lines[0].split(" ")))))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)