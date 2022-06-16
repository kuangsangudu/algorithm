'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/11 22:36       
@Author:ZHANG               
 
'''
import collections
import sys


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


sys.setrecursionlimit(10**9)


def main(lines):
    # maximum recursion depth exceeded
    def create(i_l, i_r, j_l, j_r):
        n = P[i_l]
        idx = idx2I[n]
        if idx < j_l or idx > j_r:
            return -1, None
        t = Tree(n)
        if idx-j_l > 0:
            flag, tl = create(i_l+1, i_l+idx-j_l, j_l, idx-1)
            if flag == -1:
                return -1, None
            t.left = tl
        if j_r-idx > 0:
            flag, tr = create(i_l+idx-j_l+1, i_r, idx+1, j_r)
            if flag == -1:
                return -1, None
            t.right = tr
        return 1, t

    N = int(lines[0])
    P = list(map(int, lines[1].split(" ")))
    I = list(map(int, lines[2].split(" ")))
    # P, I = lines[1], lines[2]
    idx2I = {n: i for i, n in enumerate(I)}

    if P[0] != 1:
        print(-1)
    else:
        flag, tree = create(0, len(P)-1, 0, len(P)-1)
        if flag == -1:
            print(-1)
        else:
            ret = [[0, 0] for _ in range(N+1)]

            q = collections.deque([tree])
            while q:
                a = collections.deque()
                while q:
                    b = q.popleft()
                    if b.left:
                        ret[b.val][0] = b.left.val
                        a.append(b.left)
                    if b.right:
                        ret[b.val][1] = b.right.val
                        a.append(b.right)
                q = a
            for i, j in ret[1:]:
                print(str(i) + " " + str(j))


def main1(lines):
    N = int(lines[0])
    P = list(map(int, lines[1].split(" ")))
    I = list(map(int, lines[2].split(" ")))
    idx2I = {n: i for i, n in enumerate(I)}

    if P[0] != 1:
        print(-1)
        return

    ret = [[0, 0] for _ in range(N+1)]
    q = collections.deque([[0, N-1, 0, N-1]])
    while q:
        i_l, i_r, j_l, j_r = q.popleft()
        n = P[i_l]
        idx = idx2I[n]
        if idx < j_l or idx > j_r:
            print(-1)
            return

        if idx > j_l:
            ret[n][0] = P[i_l+1]
            q.append([i_l+1, i_l+idx-j_l, j_l, idx-1])

        if idx < j_r:
            ret[n][1] = P[i_l+idx-j_l+1]
            q.append([i_l+idx-j_l+1, i_r, idx+1, j_r])

    for i, j in ret[1:]:
        print(str(i) + " " + str(j))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)

