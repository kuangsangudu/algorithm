'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 21:14       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    w1, w2, w3, h1, h2, h3 = map(int, lines[0].split(" "))
    ret = 0
    for x1 in range(1, 31):
        for x2 in range(1, 31):
            for x4 in range(1, 31):
                for x6 in range(1, 31):
                    x3 = w1 - x1 - x2
                    if x3 <= 0:
                        continue
                    x7 = h1 - x1 - x4
                    if x7 <= 0:
                        continue
                    x5 = w2 - x4 - x6
                    if x5 <= 0:
                        continue
                    x8 = h2 - x2 - x5
                    if x8 <= 0:
                        continue
                    x9 = h3 - x3 - x6
                    if x9 <= 0:
                        continue
                    if x1+x2+x3 == w1 and x4+x5+x6==w2 and x7+x8+x9==w3 and x1+x4+x7==h1 and x2+x5+x8==h2 and x3+x6+x9==h3:
                        ret += 1
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)