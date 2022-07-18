'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 21:44       
@Author:ZHANG               
 
'''
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
import functools


# it can use union-find or sortedlist to solve this problem
def main(lines):
    N, K = map(int, lines[0].split(" "))
    P = list(map(int, lines[1].split(' ')))
    re = []
    ret = [-1] * N
    for i, n in enumerate(P):
        if not re:
            if K == 1:
                ret[n-1] = i+1
            else:
                re.append([n, 1, set([n])])
            continue
        l, r = 0, len(re)-1
        while l < r:
            mid = l + (r-l)//2
            if re[mid][0] < n:
                l = mid + 1
            else:
                r = mid
        if re[l][0] < n:
            re.append([n, 1, set([n])])
        else:
            re[l][0] = n
            re[l][1] += 1
            re[l][2].add(n)
        if re[l][1] == K:
            for j in re[l][2]:
                ret[j-1] = i+1
            re.pop(l)
    for i in ret:
        print(i)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)