'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 20:53       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    n = int(lines[0])
    print(pow(2, n))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)