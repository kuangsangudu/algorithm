'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 21:35       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N, C = map(int, lines[0].split(" "))
    # bin0 means digits start with 0's result, bin1 means digits start with 1's result
    bin0 = 0
    bin1 = 2 ** 30 - 1
    for line in lines[1:]:
        t, a = map(int, line.split(" "))
        if t == 1:
            bin0 &= a
            bin1 &= a
        elif t == 2:
            bin0 |= a
            bin1 |= a
        else:
            bin0 ^= a
            bin1 ^= a

        re = 0
        for i in range(30):
            if (C >> i) & 1:
                if (bin1 >> i) & 1:
                    re += pow(2, i)
            else:
                if (bin0 >> i) & 1:
                    re += pow(2, i)
        C = re
        print(re)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)