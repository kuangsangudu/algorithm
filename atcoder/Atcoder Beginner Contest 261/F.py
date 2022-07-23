'''
@Project: algorithm   
@Description: TODO          
@Time:2022/07/23 22:22       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


class FenwickTree:
    def __init__(self, lens):
        self.arr = [0] * lens

    def lowbit(self, x):
        return x & -x

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= self.lowbit(i)
        return ret

    def update(self, i, num):
        while i < len(self.arr):
            self.arr[i] += num
            i += self.lowbit(i)

    def get_interval(self, i, j):
        return self.get(j) - self.get(i-1)


def main(lines):
    N = int(lines[0])
    C = list(map(int, lines[1].split(" ")))
    X = list(map(int, lines[2].split(" ")))
    # ret[0] save all the number
    # other save the number in the same color
    re = collections.defaultdict(list)
    for i, n in enumerate(X):
        re[0].append(n)
        re[C[i]].append(n)

    tree = FenwickTree(N+1)
    ret = 0
    for key, value in re.items():
        # let key == 0 be the number of (i, j) such that 1 <= i < j <= N and Xi > Xj ans0
        # let other be the number of (i, j) such that 1 <= i < j <= N and Xi > Xj and Ci == Cj ansi
        # then the result should be ans0 - the sum of the ansi
        if key == 0:
            for v in value:
                ret += tree.get_interval(v+1, N)
                tree.update(v, 1)
        else:
            for v in value:
                ret -= tree.get_interval(v+1, N)
                tree.update(v, 1)

        for v in value:
            tree.update(v, -1)

    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)