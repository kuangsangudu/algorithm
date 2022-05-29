'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 21:17       
@Author:ZHANG               
 
'''
import math
import sys


def getsums(N, a):
    min_a = N // a
    return (a + min_a * a) * min_a // 2


def main(lines):
    N, a, b = map(int, lines[0].split(" "))
    ret = (1 + N) * N // 2
    ret -= getsums(N, a)
    ret -= getsums(N, b)
    min_ab = a*b//math.gcd(a, b)
    ret += getsums(N, min_ab)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)