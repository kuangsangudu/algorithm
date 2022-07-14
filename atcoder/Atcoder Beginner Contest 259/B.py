'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/9 21:07       
@Author:ZHANG               
 
'''
import math
import sys


def main(lines):
    a, b, d = map(int, lines[0].split(" "))
    r = math.sqrt(a ** 2 + b ** 2)
    s = math.atan2(b, a)

    s += d / 180 * math.pi

    a = r * math.cos(s)
    b = r * math.sin(s)
    print(a, b)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)