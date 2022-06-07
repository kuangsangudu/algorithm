'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/5 16:34       
@Author:ZHANG               
 
'''
import collections
import sys


def main(lines):
    N, M = map(int, lines[0].split(" "))
    re = collections.defaultdict(list)
    for _,  line in enumerate(lines[1:M+1]):
        a, b = map(int, line.split(" "))
        re[a].append(b)
        re[b].append(a)
    Q = int(lines[M+1])
    for line in lines[M+2:]:
        x, k = map(int, line.split(" "))
        q = collections.deque([[x, 0]])
        ret = 0
        visited = {x}
        while q:
            num, s = q.popleft()
            ret += num
            for nxt in re[num]:
                if nxt not in visited and s + 1 <= k:
                    q.append([nxt, s+1])
                    visited.add(nxt)
        print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)