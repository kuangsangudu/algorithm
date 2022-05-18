'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 21:13       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N = int(lines[0])
    ret = -1
    maxs = -1
    visited = {}
    for i, s in enumerate(lines[1:], start=1):
        S, T = s.split(" ")
        if visited.get(S, -1) != -1:
            continue
        visited[S] = int(T)
        if visited[S] > maxs:
            maxs, ret = visited[S], i
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)