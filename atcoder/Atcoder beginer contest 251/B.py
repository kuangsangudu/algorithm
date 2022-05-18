'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 20:47       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, W = map(int, lines[0].split(' '))
    A = sorted(map(int, lines[1].split(" ")))
    visited = set()
    for i, num in enumerate(A):
        if num > W:
            break
        visited.add(num)
        for j, n in enumerate(A):
            if num + n > W:
                break
            if i != j:
                visited.add(num + n)
            for s, m in enumerate(A):
                if num+n+m > W:
                    break
                if i != s and j!= s and i!=j:
                    visited.add(num+n+m)
    print(len(visited))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)