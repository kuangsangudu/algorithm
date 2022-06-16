'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/11 20:51       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    R, C = map(int, lines[0].split(" "))
    A1 = list(map(int, lines[1].split(" ")))
    A2 = list(map(int, lines[2].split(" ")))
    A = [A1] + [A2]
    print(A[R-1][C-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)