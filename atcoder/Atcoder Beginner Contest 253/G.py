'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/29 22:19       
@Author:ZHANG               
 
'''
import sys


def get_position(N, L):
    sums = 0
    x, y = 1, 0
    for s in range(N-1, 0, -1):
        if sums + s < L:
            sums += s
            x += 1
        else:
            return x, L-sums


def main(lines):
    N, L, R = map(int, lines[0].split())
    x_l, y_l = get_position(N, L)
    x_r, y_r = get_position(N, R)

    ret = list(range(N+1))
    if x_l == x_r:
        for i in range(x_l + y_l, y_r+x_r+1):
            ret[x_l], ret[i] = ret[i], ret[x_l]
        print(" ".join(map(str, ret[1:])))
    else:
        for i in range(x_l + y_l, N+1):
            ret[x_l], ret[i] = ret[i], ret[x_l]

        left, right = ret[:x_l+1], ret[x_l+1:]
        for i in range(x_l+1, x_r):
            left.append(right.pop())

        ret = left + right
        for i in range(x_r, y_r+x_r+1):
            ret[x_r], ret[i] = ret[i], ret[x_r]
        print(" ".join(map(str, ret[1:])))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
