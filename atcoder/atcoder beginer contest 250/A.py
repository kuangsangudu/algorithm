'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/8 20:39       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    H, W = map(int, lines[0].split(" "))
    R, C = map(int, lines[1].split(" "))
    ret = 0
    if R - 1 > 0:
        ret += 1
    if R + 1 <= H:
        ret += 1
    if C - 1 > 0:
        ret += 1
    if C + 1 <= W:
        ret += 1
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
