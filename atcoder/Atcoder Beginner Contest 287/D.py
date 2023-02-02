'''
@Project: algorithm   
@Description: TODO          
@Time:2023/01/28 21:19       
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
    S = lines[0]
    T = lines[1]
    lens = len(S)
    lent = len(T)
    last_diff = -1
    for i in range(lent):
        if S[i+lens-lent] == "?" or T[i] == "?" or S[i+lens-lent] == T[i]:
            continue
        else:
            last_diff = i

    print("Yes" if last_diff == -1 else "No")
    flag = True
    for i in range(lent):
        if S[i] != "?" and T[i] != "?" and S[i] != T[i]:
            flag = False

        if not flag or last_diff > i:
            print("No")
        else:
            print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)