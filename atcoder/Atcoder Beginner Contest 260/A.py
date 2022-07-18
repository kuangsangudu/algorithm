'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 20:02       
@Author:ZHANG               
 
'''
import sys
import heapq


def main(lines):
    a, b, c = lines[0]
    if a != b and a != c:
        print(a)
    elif b != a and b != c:
        print(b)
    elif c != a and c != b:
        print(c)
    else:
        print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

