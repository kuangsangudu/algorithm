'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/4 21:20       
@Author:ZHANG               
 
'''
import collections
import sys


def main(lines):
    N, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    while True:
        flag = True
        for i in range(N-K):
            if A[i] > A[i+K]:
                A[i], A[i+K] = A[i+K], A[i]
                flag = False
        if flag:
            break
    if A == sorted(A):
        print("Yes")
    else:
        print("No")


def main1(lines):
    N, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    re = [[] for _ in range(K)]
    for i in range(K):
        for j in range(i, N, K):
            re[i].append(A[j])
        re[i].sort()
    flag = False
    for i in range(len(re[0])):
        pre = -1
        for j in range(len(re)):
            if i < len(re[j]):
                if re[j][i] < pre:
                    flag = True
                    break
                pre = re[j][i]
        if flag:
            break

    if flag:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)
