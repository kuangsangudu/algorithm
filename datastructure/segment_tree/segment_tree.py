'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/17 16:14       
@Author:ZHANG               
 
'''


class Segment_tree:
    def __init__(self, a):
        self.a = a
        self.Tree = [0] * (len(a) << 2)
        self._build(0, len(a) - 1, 1)
        self.len = len(self.a)
        self.lazy = [0] * (len(a) << 2)

    def push_up(self, k):
        self.Tree[k] = self.Tree[k << 1] + self.Tree[(k << 1) + 1]

    def _build(self, l, r, k):
        if l == r:
            self.Tree[k] = self.a[l]
            return
        mid = l + (r - l) // 2
        self._build(l, mid, k << 1)
        self._build(mid + 1, r, (k << 1) + 1)
        self.push_up(k)
        return

    def query(self, l, r, k, L, R):
        if l >= L and r <= R:
            return self.Tree[k]
        mid = l + (r - l) // 2
        self.push_down(k, mid - l + 1, r - mid)
        ret = 0
        if L <= mid:
            ret += self.query(l, mid, k << 1, L, R)
        if R > mid:
            ret += self.query(mid + 1, r, (k << 1) + 1, L, R)
        return ret

    def push_down(self, k, l, r):
        if self.lazy[k]:
            self.lazy[k << 1] += self.lazy[k]
            self.lazy[(k << 1) | 1] += self.lazy[k]
            self.Tree[k << 1] += self.lazy[k] * l
            self.Tree[(k << 1) | 1] += self.lazy[k] * r
            self.lazy[k] = 0

    def update(self, l, r, k, L, R, C):
        if l >= L and r <= R:
            self.Tree[k] += (r - l + 1) * C
            self.lazy[k] += C
            return
        mid = l + (r - l) // 2
        self.push_down(k, mid - l + 1, r - mid)
        if L <= mid:
            self.update(l, mid, k << 1, L, R, C)
        if R > mid:
            self.update(mid + 1, r, (k << 1) + 1, L, R, C)
        self.push_up(k)

    def update_interval(self, L, R, C):
        self.update(0, self.len - 1, 1, L, R, C)

    def update_point(self, L, C):
        self.update(0, self.len - 1, 1, L, L, C)

    def query_interval(self, L, R):
        return self.query(0, self.len - 1, 1, L, R)

    def query_point(self, L):
        return self.query(0, self.len - 1, 1, L, L)


class SegTree:
    def __init__(self, init, func, ide):
        self.n = len(init)
        self.func = func
        self.ide = ide
        self.size = 1 << (self.n - 1).bit_length()
        self.tree = [self.ide for i in range(2 * self.size)]
        for i in range(self.n):
            self.tree[self.size + i] = init[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i | 1])

    def update(self, k, x):
        k += self.size
        self.tree[k] = x
        k >>= 1
        while k:
            self.tree[k] = self.func(self.tree[2 * k], self.tree[k * 2 | 1])
            k >>= 1

    def get(self, i):
        return self.tree[i + self.size]

    def query(self, l, r):
        l += self.size
        r += self.size
        l_res = self.ide
        r_res = self.ide
        while l < r:
            if l & 1:
                l_res = self.func(l_res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_res = self.func(self.tree[r], r_res)
            l >>= 1
            r >>= 1
        return self.func(l_res, r_res)

    def debug(self, s=10):
        print([self.get(i) for i in range(min(self.n, s))])
