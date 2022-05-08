'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/7 22:19       
@Author:ZHANG               
 
'''
import sys
import heapq


def main(lines):
    N, X = map(int, lines[0].split(" "))
    re = list(map(int, lines[1].split(" ")))
    re.sort()
    maxs = re[-1]
    min_max = [[0, 0] for _ in range(len(re))]
    heap = []
    for i, n in enumerate(re):
        r, rmax = n, n
        while rmax < maxs:
            r, rmax = 2*r, 2*rmax+X
        if rmax >= maxs >= r:
            min_max[i] = [maxs, maxs]
        else:
            min_max[i] = [(rmax-X)//2, r]
        heapq.heappush(heap, [min_max[i][0], i])
    ret = float("inf")
    while heap:
        n, i = heapq.heappop(heap)
        ret = min(ret, maxs - n)
        maxs = max(min_max[i][1], maxs)
    if ret < X:
        ret = 0
    print(ret)


# wrong answer, x can be choose from 0 ~ X
def main1(lines):
    N, X = map(int, lines[0].split(" "))
    re = list(map(int, lines[1].split(" ")))
    maxs, inim = max(re), max(re)
    heapq.heapify(re)
    ret = float("inf")
    while re[0] < inim:
        num = heapq.heappop(re)
        ret = min(maxs-num, ret)
        print(maxs-num, re, maxs)
        maxs = max(maxs, num*2+X)
        heapq.heappush(re, num*2+X)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
