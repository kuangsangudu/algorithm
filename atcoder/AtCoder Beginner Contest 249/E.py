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


# difference + dp
def main2(lines):
    N, P = list(map(int, lines[0].split(" ")))
    dp = [[0] * 4100 for _ in range(3100)]
    dp[0][0] = 1
    dp[0][1] = -1
    for i in range(N):
        for j in range(N + 1):
            dp[i][j] += dp[i][j - 1]
            dp[i][j] %= P
        c = 26 if i == 0 else 25
        for j in range(N + 1):
            x = dp[i][j]
            dp[i + 2][j + 1] += c * x
            dp[i + 2][j + 10] -= c * x
            dp[i + 3][j + 10] += c * x
            dp[i + 3][j + 100] -= c * x
            dp[i + 4][j + 100] += c * x
            dp[i + 4][j + 1000] -= c * x
            dp[i + 5][j + 1000] += c * x
    ret = 0
    for i in range(N):
        ret += dp[i][N]
        ret %= P
    print(ret)


class FenwickTree:
    def __init__(self, lens, mod):
        self.arr = [0] * (lens + 1)
        self.mod = mod

    def lowbit(self, x):
        return x & -x

    def get(self, i):
        ret = 0
        while i > 0:
            ret = (ret + self.arr[i]) % self.mod
            i -= self.lowbit(i)
        return ret

    def update(self, i, num):
        while i < len(self.arr):
            self.arr[i] = self.arr[i] + num
            if self.arr[i] >= self.mod:
                self.arr[i] -= self.mod
            i += self.lowbit(i)

    def range_add(self, l, r, x):
        self.update(l, x)
        self.update(r + 1, -x)


# use Fenwick Tree TLC
def main3(lines):
    N, P = list(map(int, lines[0].split(" ")))
    Tree = [FenwickTree(3000, P) for _ in range(3006)]
    Tree[2].update(1, 26)
    Tree[2].update(10, P-26)
    Tree[3].update(10, 26)
    Tree[3].update(100, P-26)
    Tree[4].update(100, 26)
    Tree[4].update(1000, P-26)
    Tree[5].update(1000, 26)
    for i in range(1, N+1):
        for j in range(1, N+1):
            num = Tree[j].get(i)
            if not num:
                continue
            Tree[j+2].update(i+1, (25 * num) % P)
            Tree[j+2].update(i+10, (-25*num) % P)
            Tree[j+3].update(i+10, (25 * num) % P)
            Tree[j+3].update(i+100, (-25*num) % P)
            Tree[j+4].update(i+100, (25 * num) % P)
            Tree[j+4].update(i+1000, (-25*num) % P)
            Tree[j+5].update(i+1000, (25 * num) % P)
    ret = 0
    for i in range(1, N):
        ret = (ret + Tree[i].get(N)) % P
    print(ret)


class FenwickTree_mul:
    def __init__(self, lenx, leny, mod):
        self.arr = [[0 for _ in range(lenx)] for _ in range(leny)]
        self.mod = mod

    def lowbit(self, x):
        return x & -x

    def get(self, i, j):
        ret = 0
        memo_y = j
        while i > 0:
            j = memo_y
            while j > 0:
                ret += self.arr[i][j]
                if ret >= self.mod:
                    ret -= self.mod
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return ret

    def range_add(self, i, j, m, n, num):
        self.update(i, j, num)
        self.update(i, n + 1, (-num) % self.mod)
        self.update(m + 1, j, (-num) % self.mod)
        self.update(m + 1, n + 1, num)

    def update(self, i, j, num):
        memo_y = j
        while i < len(self.arr):
            j = memo_y
            while j < len(self.arr[0]):
                self.arr[i][j] += num
                if self.arr[i][j] >= self.mod:
                    self.arr[i][j] -= self.mod
                j += self.lowbit(j)
            i += self.lowbit(i)


def main(lines):
    N, P = list(map(int, lines[0].split(" ")))
    Tree = FenwickTree_mul(3001, 3001, P)
    Tree.range_add(1, 2, 9, 2, 26)
    Tree.range_add(10, 3, 99, 3, 26)
    Tree.range_add(100, 4, 999, 4, 26)
    Tree.update(1000, 5, 26)
    for i in range(1, N+1):
        for j in range(1, N+1):
            num = Tree.get(i, j)
            if not num:
                continue
            Tree.range_add(i+1, j+2, i+9, j+2, (25 * num) % P)
            Tree.range_add(i+10, j+3, i+99, j+3, (25 * num) % P)
            Tree.range_add(i+100, j+4, i+999, j+4, (25 * num) % P)
            Tree.update(i+1000, j+5, (25 * num) % P)
    ret = 0
    for i in range(1, N):
        ret = (ret + Tree.get(N, i)) % P
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


