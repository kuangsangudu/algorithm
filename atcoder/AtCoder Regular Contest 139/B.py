'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/24 21:03
@Author:ZHANG

'''

import sys


def main(lines):
    T = int(lines[0])
    for i in range(T):
        N, A, B, X, Y, Z = list(map(int, lines[i+1].split(" ")))
        a = Y / A
        b = Z / B
        if a >= X and b >= X:
            print(N*X)
        elif a >= X:
            print(N//B * Z + N % B * X)
        elif b >= X:
            print(N // A * Y + N % A * X)
        else:
            if a >= b:
                A, B = B, A
                Y, Z = Z, Y
            ret = float("inf")
            if N // A < A-1:
                for i in range(N//A+1):
                    amins = N - i * A
                    ret = min(ret, i * Y + amins//B * Z + amins % B * X)
            else:
                for i in range(A):
                    if i * B > N:
                        break
                    bmins = N - i * B
                    ret = min(ret, i * Z + bmins//A * Y + bmins % A * X)
            print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
