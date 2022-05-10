'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/8 22:08       
@Author:ZHANG               
 
'''
# reference to other's id, use hash.
# later I will update something for Zobrist Hash
# I first consider use segment tree to solve this problem.
import sys


def f(a):
    temp = set()
    s = 0
    Mod = 10 ** 9 + 7
    ret = [0] * (len(a)+1)
    for i, n in enumerate(a, start=1):
        if n not in temp:
            temp.add(n)
            s = (s + n * (n + 1346) * (n + 9185)) % Mod
        ret[i] = s
    return ret


def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    b = list(map(int, lines[2].split(' ')))
    Q = int(lines[3])
    ra = f(a)
    rb = f(b)

    for X in lines[4:]:
        x, y = map(int, X.split(' '))
        if ra[x] == rb[y]:
            print("Yes")
        else:
            print('No')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
