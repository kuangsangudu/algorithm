'''
@Project: algorithm   
@Description: TODO          
@Time:2022/09/03 21:03       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    s = lines[0]
    if s[0] == "1":
        print("No")
    else:
        re = [False] * 7
        re[0] = int(s[6]) == 1
        re[1] = int(s[3]) == 1
        re[2] = (int(s[7]) + int(s[1])) >= 1
        re[3] = (int(s[0]) + int(s[4])) >= 1
        re[4] = (int(s[2]) + int(s[8])) >= 1
        re[5] = int(s[5]) == 1
        re[6] = int(s[9]) == 1
        i = 0
        while i < len(re):
            if not re[i]:
                i += 1
            elif i+1 < len(re) and re[i+1]:
                i += 1
            elif i+1 < len(re) and not re[i+1]:
                j = i + 2
                while j < len(re) and not re[j]:
                    j += 1
                if j < len(re):
                    print("Yes")
                    return
                break
            else:
                i += 1
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
