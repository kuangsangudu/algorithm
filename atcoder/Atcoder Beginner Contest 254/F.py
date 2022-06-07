'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/5 17:07       
@Author:ZHANG               
 
'''
import math
import sys


# my implement, because of the iterate, time cost is a lot.
class segmentTree:
    def __init__(self, a):
        self.a = [0] * len(a)
        self.a[0] = a[0]
        for i in range(1, len(a)):
            self.a[i] = abs(a[i] - a[i-1])
        self.Tree = [0] * ((len(a)) << 2)
        self._build(0, len(a)-1, 1)

    def push_up(self, i):
        self.Tree[i] = math.gcd(self.Tree[i << 1], self.Tree[(i << 1) + 1])
        return

    def _build(self, l, r, k):
        if l == r:
            self.Tree[k] = self.a[l]
            return
        mid = l + (r-l)//2
        self._build(l, mid, k << 1)
        self._build(mid+1, r, (k << 1)+1)
        self.push_up(k)
        return

    def query(self, l, r, L, R, k):
        if l >= L and r <= R:
            return self.Tree[k]
        mid = l + (r - l) // 2
        i, j = -1, -1
        if L <= mid:
            i = self.query(l, mid, L, R, k << 1)
        if R > mid:
            j = self.query(mid+1, r, L, R, (k << 1)+1)

        if i != -1 and j != -1:
            return math.gcd(i, j)
        elif i != -1:
            return i
        elif j != -1:
            return j
        else:
            return -1

    def query_interval(self, l, r):
        return self.query(0, len(self.a)-1, l, r, 1)


# other's implement, reverse update
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query_interval(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def get_diff(arr):
    ret = [0] * len(arr)
    ret[0] = arr[0]
    for i in range(1, len(ret)):
        ret[i] = abs(arr[i] - arr[i - 1])
    return ret


def main(lines):
    N, Q = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    B = list(map(int, lines[2].split(" ")))
    # tree_a = segmentTree(A)
    # tree_b = segmentTree(B)
    diff_a = []
    tree_a = SegTree(get_diff(A), math.gcd, 0)
    tree_b = SegTree(get_diff(B), math.gcd, 0)
    for query in lines[3:]:
        h1, h2, w1, w2 = map(int, query.split(" "))
        ret = A[h1-1] + B[w1-1]
        if w2 > w1:
            ret = math.gcd(ret, tree_b.query_interval(w1, w2))
        if h2 > h1:
            ret = math.gcd(ret, tree_a.query_interval(h1, h2))
        print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
