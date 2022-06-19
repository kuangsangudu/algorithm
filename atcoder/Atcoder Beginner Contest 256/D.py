'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/18 21:27       
@Author:ZHANG               
 
'''

import sys


class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        if not self.ranges:
            return 0, -1
        l, r = 0, len(self.ranges) - 1
        while l < r:
            mid = l + (r-l)//2
            if self.ranges[mid][1] < left:
                l = mid + 1
            else:
                r = mid
        i = l if self.ranges[l][1] >= left else l + 1
        l, r = 0, len(self.ranges) - 1
        while l < r:
            mid = l + (r-l+1)//2
            if self.ranges[mid][0] <= right:
                l = mid
            else:
                r = mid - 1
        j = l - 1 if self.ranges[l][0] > right else l
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]


def main(lines):
    N = int(lines[0])
    L = []
    for line in lines[1:]:
        l, r = map(int, line.split(' '))
        L.append([l, r])
    L.sort()
    ret = []
    for l, r in L:
        if ret and ret[-1][1] >= l:
            ret[-1][1] = max(ret[-1][1], r)
        else:
            ret.append([l, r])
    for l, r in ret:
        print(str(l) + " " + str(r))


def main1(lines):
    N = int(lines[0])
    L = [0] * (2 * 10**5+2)
    for i, line in enumerate(lines[1:]):
        l, r = map(int, line.split(' '))
        L[l] += 1
        L[r] -= 1
    sums = 0
    pre = -1
    for i, n in enumerate(L):
        if n and sums == 0:
            pre = i
        sums += n
        if sums == 0 and pre != -1:
            print(pre, i)
            pre = -1


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)
