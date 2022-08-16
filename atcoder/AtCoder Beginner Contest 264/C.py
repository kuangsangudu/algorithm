'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/13 21:16       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
import itertools
sys.setrecursionlimit(10 ** 6)
import functools


def getSubSet(A, row, col):
    B = []
    for i in row:
        B.append([])
        for j in col:
            B[-1].append(A[i][j])
    return B


def compare(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True


def main(lines):
    H1, W1 = map(int, lines[0].split(" "))
    A = []
    for line in lines[1: H1+1]:
        A.append(list(map(int, line.split(" "))))
    H2, W2 = map(int, lines[H1+1].split(" "))
    B = []
    for line in lines[H1+2:]:
        B.append(list(map(int, line.split(" "))))

    if H1 < H2 or W1 < W2:
        print("No")
        return

    for n in itertools.combinations(range(len(A)), len(B)):
        for m in itertools.combinations(range(len(A[0])), len(B[0])):
            asub = getSubSet(A, n, m)
            if compare(asub, B):
                print("Yes")
                return
    print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)