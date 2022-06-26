'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/25 21:08       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, K, Q = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    L = list(map(int, lines[2].split(" ")))
    for i, n in enumerate(L):
        if A[n-1] < N:
            if n == len(A):
                A[n-1] += 1
            elif A[n] > A[n-1]+1:
                A[n - 1] += 1
    print(" ".join(map(str, A)))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)