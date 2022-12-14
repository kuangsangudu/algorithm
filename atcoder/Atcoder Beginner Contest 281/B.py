'''
@Project: algorithm   
@Description: TODO          
@Time:2022/12/10 21:01       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 9)


def main(lines):
    s = lines[0]
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and 100000 <= int(s[1:-1]) <= 999999 and len(s) == 8:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
