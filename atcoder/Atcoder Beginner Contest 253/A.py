'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 20:57       
@Author:ZHANG               
 
'''
import heapq
import sys


def main(lines):
    A, B, C = map(int, lines[0].split(" "))
    if A <= B <= C or C <= B <= A:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
