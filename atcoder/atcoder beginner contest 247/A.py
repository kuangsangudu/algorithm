'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/14 23:46       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    ret = ["0"] * len(lines[0])
    l = 0
    for i, n in enumerate(lines[0]):
        if n == "1" and l:
            ret[i] = "1"
        elif l:
            ret[i] = "1"
            l = 0
        elif n == "1":
            l = 1
    print("".join(ret))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
