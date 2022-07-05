'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/2 21:19       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, Q = map(int, lines[0].split(" "))
    s = lines[1]
    start = 0
    for query in lines[2:]:
        idx, num = map(int, query.split(" "))
        if idx == 1:
            start = (start + N - num) % N
        else:
            i = (start + num - 1) % N
            print(s[i])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
