'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/21 20:56       
@Author:ZHANG               
 
'''
import sys
import heapq


def main(lines):
    N, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    B = list(map(int, lines[2].split(" ")))
    maxs = max(A)
    for i, num in enumerate(A):
        if num == maxs:
            if i+1 in B:
                print("Yes")
                break
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
