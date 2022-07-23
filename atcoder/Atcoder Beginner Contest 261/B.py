'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 21:04       
@Author:ZHANG               
 
'''
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    N = int(lines[0])
    graph = lines[1:]
    flag = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == "W":
                if graph[j][i] != "L":
                    print("incorrect")
                    flag = False
                    break
            elif graph[i][j] == "L":
                if graph[j][i] != "W":
                    print("incorrect")
                    flag = False
                    break
            else:
                if graph[j][i] != "D":
                    print("incorrect")
                    flag = False
                    break
        if not flag:
            break
    else:
        print("correct")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)