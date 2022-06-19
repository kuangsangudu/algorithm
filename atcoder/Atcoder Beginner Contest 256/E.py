'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 22:05       
@Author:ZHANG               
 
'''
import sys


# https://atcoder.jp/contests/abc256/editorial/4145 graph id


class Union:
    def __init__(self, lens):
        self.Union = list(range(lens))
        self.rank = [1] * lens

    def find(self, x):
        while self.Union[x] != x:
            x = self.Union[x]
        return x

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return
        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x
        self.rank[par_x] += self.rank[par_y]
        self.Union[par_y] = par_x

    def is_union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return True
        return False


def main(lines):
    N = int(lines[0])
    X = list(map(int, lines[1].split(' ')))
    C = list(map(int, lines[2].split(" ")))
    union = Union(N)
    ret = 0
    for i in range(N):
        x, y = i, X[i]-1
        if not union.is_union(x, y):
            union.union(x, y)
        else:
            ans = C[x]
            while y != x:
                ans = min(ans, C[y])
                y = X[y]-1
            ret += ans
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
