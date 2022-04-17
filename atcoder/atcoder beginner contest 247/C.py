'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/14 23:46
@Author:ZHANG

'''
import sys


def main(lines):
    N = int(lines[0])
    if N == 1:
        print("1")
    else:
        r = "1 "
        for i in range(2, N+1):
            r = r + str(i) + " " + r
        print(r)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
