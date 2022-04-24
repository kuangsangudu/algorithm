'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 21:27       
@Author:ZHANG               
 
'''
'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 20:36
@Author:ZHANG

'''

import sys


def xunzhao(S, k):
    ret = 0
    for i in range(26):
        a = chr(97+i)
        re = 0
        for s in S:
            if a in s:
                re += 1
        if re == k:
            ret += 1
    return ret


def main(lines):
    N, K = list(map(int, lines[0].split(" ")))
    S = lines[1:]
    ret = 0
    for i in range(1, 1<<len(S)):
        s = []
        for j in range(N):
            if i & (1<<j):
                s.append(S[j])
        print(s, xunzhao(S, K))
        ret = max(ret, xunzhao(s, K))
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
