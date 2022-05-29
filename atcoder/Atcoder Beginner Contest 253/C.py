'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 21:07       
@Author:ZHANG               
 
'''
import collections
import heapq
import sys


def main(lines):
    Q = int(lines[0])
    min_h = []
    max_h = []
    re = collections.Counter()
    for query in lines[1:]:
        if query[0] == "1":
            _, x = map(int, query.split(" "))
            if re.get(x, -1) > 0:
                re[x] += 1
            else:
                heapq.heappush(max_h, -x)
                heapq.heappush(min_h, x)
                re[x] = 1
        elif query[0] == "2":
            _, x, c = map(int, query.split(" "))
            mins = min(c, re.get(x, -1))
            if mins > 0:
                re[x] -= mins
        else:
            while min_h and re[min_h[0]] == 0:
                heapq.heappop(min_h)
            while max_h and re[-max_h[0]] == 0:
                heapq.heappop(max_h)
            print(-max_h[0]-min_h[0])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)