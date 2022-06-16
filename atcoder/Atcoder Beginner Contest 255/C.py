'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/11 21:14       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    X, A, D, N = map(int, lines[0].split(" "))
    if D == 0:
        print(abs(X-A))
    else:
        mins = min(A, A + D * (N-1))
        maxs = max(A, A + D * (N-1))
        left = (X-A) % abs(D)
        right = abs(D) - (X-A) % abs(D)
        if X <= mins:
            print(mins-X)
        elif X >= maxs:
            print(X-maxs)
        elif left <= right:
            print(left)
        else:
            print(right)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)