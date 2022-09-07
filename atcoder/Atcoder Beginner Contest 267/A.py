'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 20:55       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    s = lines[0]
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    else:
        print(1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
