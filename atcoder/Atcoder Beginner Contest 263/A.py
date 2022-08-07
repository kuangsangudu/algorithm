'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/06 20:05       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    line = lines[0].split(" ")
    c = collections.Counter(line)
    if len(c) == 2 and c[list(c.keys())[0]] in [2, 3]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)