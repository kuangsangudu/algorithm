'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/14 23:46
@Author:ZHANG

'''
import collections
import sys


def main(N, P, Q):
    re = collections.defaultdict(int)
    Mod = 998244353
    sums = [1, 1, 3]
    for i in range(N-2):
        sums.append((sums[-1] + sums[-2]) % Mod)
    ret = 1
    for i in range(N):
        re[P[i]] = Q[i]
    visited = set()
    for i in range(1, N+1):
        if i in visited:
            continue
        j = 0
        s = i
        while s not in visited:
            visited.add(s)
            j += 1
            s = re[s]
        ret = ret * sums[j] % Mod
    print(ret)


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    main(N, P, Q)
