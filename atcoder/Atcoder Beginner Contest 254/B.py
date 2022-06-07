'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/4 21:02       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N = int(lines[0])
    A = [1]
    print(str(1))
    for i in range(1, N):
        B = [1] * (i+1)
        for j in range(1, i):
            B[j] = A[j-1] + A[j]
        print(" ".join(map(str, B)))
        A = B


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
