'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 20:47       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    s = lines[0]
    ret = ""
    while len(ret) < 6:
        ret += s
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
