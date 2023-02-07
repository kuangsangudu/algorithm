'''
@Project: algorithm   
@Description: TODO          
@Time:2023/02/04 21:17       
@Author:ZHANG               
 
'''
import bisect
import collections
import copy
import fractions
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


# 差分思想 https://atcoder.jp/contests/abc288/editorial/5676
def main(lines):
    N, K = map(int, lines[0].split(" "))
    A = [0] + list(map(int, lines[1].split(" "))) + [0]
    arr = [0] * (N+1)
    for i in range(N+1):
        arr[i] = A[i+1]-A[i]

    pre_sums = [[0] * (N+2) for _ in range(K)]
    for i in range(K):
        pre_sums[i][i+1] = arr[i]
        for j in range(i+1, N+1):
            if j % K == i:
                pre_sums[i][j+1] = pre_sums[i][j] + arr[j]
            else:
                pre_sums[i][j+1] = pre_sums[i][j]

    Q = int(lines[2])
    for line in lines[3:]:
        l, r = map(int, line.split(" "))
        r += 1
        flag = False
        for i in range(K):
            nums = pre_sums[i][r] - pre_sums[i][l-1]
            if (l-1) % K == i:
                nums += A[l-1]
            if (r-1) % K == i:
                nums -= A[r]
            if nums != 0:
                flag = True
                break
        if flag:
            print("No")
        else:
            print("Yes")


# 不变量思路
def main1(lines):
    def get_value(i, l, r):
        return pre_sums[i][r] - pre_sums[i][l-1]

    N, K = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))

    pre_sums = [[0] * (N+1) for _ in range(K)]
    for i in range(K):
        for j in range(N):
            pre_sums[i][j+1] += pre_sums[i][j] + (A[j] if j % K == i else 0)

    Q = int(lines[2])
    for line in lines[3:]:
        l, r = map(int, line.split(" "))
        t = get_value(0, l, r)
        flag = False
        for i in range(1, K):
            if get_value(i, l, r) != t:
                flag = True
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