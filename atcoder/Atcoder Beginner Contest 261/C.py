'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 21:12       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    re = collections.defaultdict(int)
    for s in lines[1:]:
        if re.get(s, -1) == -1:
            print(s)
            re[s] = 1
        else:
            while re.get(s+"("+str(re[s])+")", -1) != -1:
                re[s] += 1
            s = s+"("+str(re[s])+")"
            re[s] = 1
            print(s)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)