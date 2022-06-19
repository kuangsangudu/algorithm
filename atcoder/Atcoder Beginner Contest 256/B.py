'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 21:01       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    re = [0] * 4
    ret = 0
    for num in A:
        re[0] = 1
        for i in range(3, -1, -1):
            if re[i]:
                if i + num < 4:
                    re[i+num] = 1
                    re[i] = 0
                else:
                    ret += 1
                    re[i] = 0
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)