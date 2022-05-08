'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/8 21:26       
@Author:ZHANG               
 
'''
import sys
import collections


def main(lines):
    N, Q = map(int, lines[0].split(" "))
    re = collections.defaultdict(int)
    ret = list(range(1, N+1))
    for i, n in enumerate(ret):
        re[n] = i
    for x in map(int, lines[1:]):
        n, ne = re[x], re[x]+1 if re[x]+1 < N else re[x]-1
        re[x] = ne
        re[ret[ne]] = n
        ret[n], ret[ne] = ret[ne], ret[n]
    print(" ".join(list(map(str, ret))))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)