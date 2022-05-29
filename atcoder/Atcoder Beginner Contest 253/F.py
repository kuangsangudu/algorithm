'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 22:06       
@Author:ZHANG               
 
'''
import sys


# class FenwickTree:
#     def __init__(self, N, M):
#         self.arr = [[0 for i in range(M+1)] for _ in range(N+1)]
#
#     def lowbit(self, x):
#         return x & -x
#
#     def get(self, i, j):
#         ret = 0
#         memo_y = j
#         while i > 0:
#             j = memo_y
#             while j > 0:
#                 ret += self.arr[i][j]
#                 j -= self.lowbit(j)
#             i -= self.lowbit(i)
#         return ret
#
#     def range_add(self, i, j, m, n, num):
#         self.update(i, j, num)
#         self.update(i, n + 1, -num)
#         self.update(m + 1, j, -num)
#         self.update(m + 1, n + 1, num)
#
#     def update(self, i, j, num):
#         memo_y = j
#         while i < len(self.arr):
#             j = memo_y
#             while j < len(self.arr[0]):
#                 self.arr[i][j] += num
#                 j += self.lowbit(j)
#             i += self.lowbit(i)

class FenwickTree:
    def __init__(self, lens):
        self.arr = [0] * (lens+1)

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

    def range_add(self, l, r, x):
        self.update(l, x)
        self.update(r+1, -x)


def main(lines):
    N, M, Q = map(int, lines[0].split(" "))
    # Tree is used to Interval accumulation and summation
    Tree = FenwickTree(M)
    # rows is the latest row list, rows[i] = [query[i], number]
    rows = [[-1, 0]] * (N+1)
    # sub is used to get all the query3 connected to the query 2
    sub = [[] for _ in range(Q)]
    # query store all the require value.
    query = [[] for _ in range(Q)]
    ans = []
    for idx, line in enumerate(lines[1:]):
        if line[0] == "1":
            _, l, r, x = map(int, line.split(" "))
            query[idx] = [_, l, r, x]
        elif line[0] == "2":
            _, i, x = map(int, line.split(" "))
            rows[i] = [idx, x]
            query[idx] = [_, i, x]
        else:
            _, i, j = map(int, line.split(" "))
            query[idx] = [_, i, j, len(ans)]
            if rows[i][0] >= 0:
                sub[rows[i][0]].append(idx)
            ans.append(rows[i][1])

    # print(query, ans, sub, rows)
    for i in range(Q):
        if query[i][0] == 1:
            Tree.range_add(query[i][1], query[i][2], query[i][3])
        elif query[i][0] == 2:
            for nxt in sub[i]:
                ans[query[nxt][-1]] -= Tree.get(query[nxt][2])
        else:
            ans[query[i][-1]] += Tree.get(query[i][2])
            print(ans[query[i][-1]])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)