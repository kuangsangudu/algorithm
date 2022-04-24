'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 21:27
@Author:ZHANG

'''
import collections
import sys


# wrong answer
# not consider about the minus problem
def main1(lines):
    N, P = list(map(int, lines[0].split(" ")))
    ret = 0
    dp = [[[0 for _ in range(3)] for _ in range(26)] for _ in range(N+1)]
    for i in range(26):
        dp[1][i][1] = 1
    for i in range(2, N+1):
        for j in range(26):
            for c in range(1, 3):
                if c == 1:
                    for m in range(26):
                        for n in range(1, 3):
                            if m != j:
                                dp[i][j][c] = (dp[i][j][c] + dp[i-1][m][n]) % P
                else:
                    dp[i][j][c] = dp[i-1][j][1]
    print((26 ** N - sum(map(sum, dp[-1]))) % P)


def main(lines):
    N, P = list(map(int, lines[0].split(" ")))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


