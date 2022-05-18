'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 21:44       
@Author:ZHANG               
 
'''
import sys


def main1(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(' ')))

    # only use An
    dp = [[float("inf"), float("inf")] for _ in range(N)]
    dp[0][0] = 0
    for i in range(1, N):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + A[i]
    ret = dp[-1][1]

    # must use A0 (A0 AND AN all used is ok)
    dp = [[float("inf"), float("inf")] for _ in range(N)]
    dp[0][1] = A[0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + A[i]
    ret = min(ret, dp[-1][1], dp[-1][0])
    print(ret)


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(' ')))

    # only use An
    pre0, pre1 = 0, float("inf")
    for i in range(1, N):
        now0, now1 = pre1, min(pre0, pre1) + A[i]
        pre0, pre1 = now0, now1
    ret = pre1

    # must use A0 (A0 AND AN all used is ok)
    pre0, pre1 = float("inf"), A[0]
    for i in range(1, N):
        now0, now1 = pre1, min(pre0, pre1) + A[i]
        pre0, pre1 = now0, now1
    ret = min(ret, pre0, pre1)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
