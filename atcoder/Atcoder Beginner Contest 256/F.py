'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 22:10       
@Author:ZHANG               
 
'''
import sys


class FenwickTree:
    def __init__(self, lens, Mod):
        self.arr = [0] * (lens+1)
        self.mod = Mod

    def lowbit(self, x):
        return x & -x

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= self.lowbit(i)
        return ret

    def update(self, i, num):
        num = num % self.mod
        while i < len(self.arr):
            self.arr[i] = (self.arr[i] + num) % self.mod
            i += self.lowbit(i)


def main(lines):
    N, Q = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    lens = len(A)
    Mod = 998244353
    Treea = FenwickTree(lens, Mod)
    Treeia = FenwickTree(lens, Mod)
    Treei2a = FenwickTree(lens, Mod)
    inv2 = pow(2, Mod - 2, Mod)

    for i, num in enumerate(A, start=1):
        Treea.update(i, num)
        Treeia.update(i, i * num)
        Treei2a.update(i, i**2 * num)
    for query in lines[2:]:
        if query[0] == '1':
            _, x, v = map(int, query.split(" "))
            numa = Treea.get(x)-Treea.get(x-1)
            Treea.update(x, -numa)
            Treeia.update(x, -x*numa)
            Treei2a.update(x, -x**2*numa)
            Treea.update(x, v)
            Treeia.update(x, x*v)
            Treei2a.update(x, x**2*v)
        else:
            _, x = map(int, query.split(" "))
            print((inv2*Treei2a.get(x) - (2*x+3) * Treeia.get(x) * inv2 + (x+1)*(x+2)//2 * Treea.get(x)) % Mod)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
