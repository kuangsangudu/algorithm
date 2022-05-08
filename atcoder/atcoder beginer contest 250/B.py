'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/8 21:18       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, A, B = map(int, lines[0].split(" "))
    start = 0
    for i in range(N):
        start ^= 1
        for _ in range(A):
            strs = ""
            s = start
            for j in range(N):
                if s == 1:
                    strs += "." * B
                else:
                    strs += "#" * B
                s ^= 1
            print(strs)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
