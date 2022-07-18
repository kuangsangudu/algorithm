'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 21:05       
@Author:ZHANG               
 
'''
import sys
import heapq


def main(lines):
    N, X, Y, Z = map(int, lines[0].split(" "))
    A = [[n, i] for i, n in enumerate(list(map(int, lines[1].split(" "))))]
    B = [[n, i] for i, n in enumerate(list(map(int, lines[2].split(' '))))]
    C = [[A[i][0]+B[i][0], i] for i in range(N)]
    A.sort(key=lambda x: [-x[0], x[1]])
    visited = set()
    for i in range(X):
        visited.add(A[i][1])

    B.sort(key=lambda x: [-x[0], x[1]])
    for i in range(N):
        if B[i][1] in visited:
            continue
        if Y == 0:
            break
        Y -= 1
        visited.add(B[i][1])

    C.sort(key=lambda x: [-x[0], x[1]])
    for i in range(len(C)):
        if C[i][1] in visited:
            continue
        if Z == 0:
            break
        Z -= 1
        visited.add(C[i][1])
    for i in sorted(visited):
        print(i+1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)