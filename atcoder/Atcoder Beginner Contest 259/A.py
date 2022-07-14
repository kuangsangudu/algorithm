'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/9 20:29       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, M, X, T, D = map(int, lines[0].split(" "))
    if N < X:
        N, T = X, T + (X-N) * D
    if M >= X:
        print(T)
    else:
        print(T - (X-M) * D)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
