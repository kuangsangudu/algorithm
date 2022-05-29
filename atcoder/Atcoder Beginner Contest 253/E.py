'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 21:34       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, M, K = map(int, lines[0].split(" "))
    dp = [[0 for _ in range(M+2)] for _ in range(N)]
    for i in range(1, M+1):
        dp[0][i] = 1
    Mod = 998244353
    for i in range(1, N):
        sum_l = 0
        sum_r = sum(dp[i-1][1+K:])
        for j in range(1, M+1):
            dp[i][j] = sum_l + sum_r
            sum_l = (sum_l + (dp[i-1][j-K+1] if j-K+1 >= 1 else 0)) % Mod
            sum_r = (sum_r - (dp[i-1][j+K] if j+K <= M else 0)) % Mod
    print(sum(dp[-1]) % Mod)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)