'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/9 21:45       
@Author:ZHANG               
 
'''
import sys


class Union:
    def __init__(self, N):
        self.u = list(range(N))
        self.rank = [1] * N

    def find(self, x):
        while self.u[x] != x:
            x = self.u[x]
        return x

    def union(self, a, b):
        par_a, par_b = self.find(a), self.find(b)
        if par_a == par_b:
            return
        if self.rank[par_a] < self.rank[par_b]:
            par_a, par_b = par_b, par_a
        self.u[par_b] = par_a
        self.rank[par_a] += self.rank[par_b]


def points_dis(x, y, m, n):
    return (x-m)**2 + (y-n)**2


def main(lines):
    N = int(lines[0])
    sx, sy, tx, ty = map(int, lines[1].split(' '))
    union = Union(N)
    s = []
    t = []
    rs = []
    for i, line in enumerate(lines[2:]):
        x, y, r = map(int, line.split(' '))
        rs.append([x, y, r])
        if points_dis(sx, sy, x, y) == r**2:
            s.append(i)
        if points_dis(tx, ty, x, y) == r**2:
            t.append(i)
    target = s[0]
    visited = set()
    while s:
        num = s.pop()
        if num in visited:
            continue
        visited.add(num)
        for i, line in enumerate(rs):
            if i not in visited and (max(line[2], rs[num][2]) - min(line[2], rs[num][2]))**2 <= points_dis(rs[num][0], rs[num][1], line[0], line[1]) <= (line[2] + rs[num][2])**2:
                union.union(num, i)
                s.append(i)

    target = union.find(target)
    for nxt in t:
        if union.find(nxt) == target:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)