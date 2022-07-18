'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/18 0:55       
@Author:ZHANG               
 
'''
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


def main(lines):
    S, T, M = map(int, lines[0].split(" "))
    arr = [[] for _ in range(S+1)]
    for line in lines[1:]:
        u, v = map(int, line.split(" "))
        arr[u].append(v-S)

    dp = [[0] * (T+1) for _ in range(T+1)]
    # the Pigeonhole Principle. it must end at O(T**2)
    for i in range(1, S+1):
        for m in arr[i]:
            for n in arr[i]:
                if m == n:
                    continue
                if dp[m][n]:
                    print(str(i) + " " + str(m+S) + " " + str(n+S) + " " + str(dp[m][n]))
                    return
                dp[m][n] = i
    print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)