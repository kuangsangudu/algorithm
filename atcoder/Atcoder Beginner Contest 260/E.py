'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 22:07       
@Author:ZHANG               
 
'''
'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/17 21:44       
@Author:ZHANG               

'''
import sys
import heapq
import functools

sys.setrecursionlimit(10 ** 6)


def main(lines):
    N, M = map(int, lines[0].split(" "))
    graph = [[] for _ in range(M+1)]
    for i, line in enumerate(lines[1:]):
        a, b = map(int, line.split(" "))
        graph[a].append(i)
        graph[b].append(i)

    re = [0] * (N+1)
    j = 0
    sums = [0] * (M+2)
    nums = N

    # slide windows to get the smallest success segment, sums array will get the accumulated value
    for i in range(1, M+1):
        while nums and j < M+1:
            for nxt in graph[j]:
                if re[nxt] == 0:
                    nums -= 1
                re[nxt] += 1
            j += 1
        if nums > 0:
            break
        sums[j-i] += 1
        sums[M+2-i] -= 1
        for nxt in graph[i]:
            re[nxt] -= 1
            if re[nxt] == 0:
                nums += 1

    for i in range(1, M+1):
        sums[i] += sums[i-1]
    print(" ".join(list(map(str, sums[1:-1]))))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)