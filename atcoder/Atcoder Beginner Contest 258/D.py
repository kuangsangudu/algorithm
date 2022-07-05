'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/2 21:28       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, X = map(int, lines[0].split(" "))
    ret = float("inf")
    sums = 0
    i = 0
    for line in lines[1:]:
        i += 1
        movietime, gametime = map(int, line.split(" "))
        sums += movietime + gametime
        ret = min(ret, sums + gametime * (X-i))
        if i == X:
            break
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
