'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 20:08       
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


def main(lines):
    N = int(lines[0])
    S = lines[1:]
    agree_num = S.count("For")
    if agree_num > len(S)//2:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)