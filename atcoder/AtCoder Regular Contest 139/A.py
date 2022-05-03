'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/24 21:03       
@Author:ZHANG               
 
'''

import sys


def xunzhao(n, pre):
    ret = 1 << n
    if ret > pre:
        return ret
    i = n+1
    while ret <= pre:
        ret += 1 << i
        i += 1

    i -= 1
    for j in range(i, n, -1):
        if ret - (1<<j) > pre:
            ret -= (1<<j)
    return ret


def main(lines):
    N = int(lines[0])
    T = list(map(int, lines[1].split(" ")))
    pre = 0
    for n in T:
        ret = xunzhao(n, pre)
        pre = ret
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)