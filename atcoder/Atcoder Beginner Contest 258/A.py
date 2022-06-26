'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/25 19:30       
@Author:ZHANG               
 
'''
import collections
import sys


def main(lines):
    N, X = map(int, lines[0].split(" "))
    X = (X-1) % (N*26) // N
    print(chr(65+X))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)