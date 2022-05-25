'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/21 22:05       
@Author:ZHANG               
 
'''
import collections
import sys
import heapq


class Union:
    def __init__(self, lens):
        self.union = list(range(lens))
        self.rank = [1] * lens
        self.maxrank = 1

    def find(self, x):
        while self.union[x] != x:
            x = self.union[x]
        return x

    def unions(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if self.rank[par_x] <= self.rank[par_y]:
            par_x, par_y = par_y, par_x
        self.union[par_y] = par_x
        self.rank[par_x] += self.rank[par_y]
        self.maxrank = max(self.maxrank, self.rank[par_x])


# I made a mistake, I first thought of this problem as a spanning tree problem,
# but later I find it's just a min-path problem.
def main1(lines):
    N, M = map(int, lines[0].split(' '))
    re = []
    start = 1
    for line in lines[1:]:
        A, B, C = map(int, line.split(" "))
        re.append([C, A, B, start])
        start += 1
    re.sort()
    union = Union(N+1)
    ret = []
    for C, A, B, road in re:
        if union.find(A) != union.find(B):
            ret.append(road)
            union.unions(A, B)
        if union.maxrank == N:
            break
    print(" ".join([str(i) for i in ret]))


def main(lines):
    N, M = map(int, lines[0].split(' '))
    re = collections.defaultdict(list)
    start = 1
    for line in lines[1:]:
        A, B, C = map(int, line.split(" "))
        re[A].append([B, C, start])
        re[B].append([A, C, start])
        start += 1
    Q = [[0, 1, -1]]
    ret = []
    visited = set()
    while Q:
        num, i, road = heapq.heappop(Q)
        if i in visited:
            continue
        visited.add(i)
        ret.append(road)
        for nxt in re[i]:
            if nxt[0] not in visited:
                heapq.heappush(Q, [num+nxt[1], nxt[0], nxt[2]])
    print(" ".join([str(i) for i in ret[1:]]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)