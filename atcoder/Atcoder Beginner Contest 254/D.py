'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/4 22:01       
@Author:ZHANG               
 
'''
import sys


def get_max_square(x, N):
    for i in range(int(N**0.5), 0, -1):
        if x % (i**2) == 0:
            return i**2


def main(lines):
    N = int(lines[0])
    ret = 0
    count = [0] * (N+1)
    for i in range(1, N+1):
        num = get_max_square(i, N)
        count[i//num] += 1
    for num in count:
        ret += num ** 2
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
