'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/25 21:42       
@Author:ZHANG               
 
'''
import heapq
import math
import sys


def main(lines):
    N = int(lines[0])
    re = []
    for line in lines[1:]:
        re.append(list(map(int, line.split(" "))))
    ret = float("inf")
    for i in range(len(re)):
        ree = []
        visited = [float("inf")] * len(re)
        visited[i] = 0
        for j in range(len(re)):
            if i != j:
                heapq.heappush(ree, [math.ceil((abs(re[j][0]-re[i][0])+abs(re[j][1]-re[i][1]))/re[i][2]), j])
        while ree:
            num, j = heapq.heappop(ree)
            if visited[j] < num:
                continue
            visited[j] = num
            for nxt in range(len(re)):
                if nxt == i or nxt == j:
                    continue
                a = max(num, math.ceil((abs(re[j][0]-re[nxt][0])+abs(re[j][1]-re[nxt][1]))/re[j][2]))
                if visited[nxt] <= a:
                    continue
                else:
                    visited[nxt] = a
                    heapq.heappush(ree, [a, nxt])
        ret = min(ret, max(visited))
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
