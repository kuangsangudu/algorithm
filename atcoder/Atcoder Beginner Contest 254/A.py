'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/4 20:25       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N = lines[0]
    print(N[-2:])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
