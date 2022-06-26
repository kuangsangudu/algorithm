'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/25 21:20       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N = int(lines[0])
    S = lines[1]
    W = list(map(int, lines[2].split(" ")))
    more_a = 0
    re = []
    for i, n in enumerate(W):
        re.append([n, S[i]])
        if S[i] == "1":
            more_a += 1
    re.sort()
    i = 0
    pre = 0
    ret = 0
    while i < len(W):
        ret = max(ret, pre+more_a)
        pre += 1 if re[i][1] == "0" else 0
        more_a -= 1 if re[i][1] == "1" else 0
        while i+1 < len(W) and re[i+1][0] == re[i][0]:
            i += 1
            pre += 1 if re[i][1] == "0" else 0
            more_a -= 1 if re[i][1] == "1" else 0
        i += 1
    ret = max(ret, pre + more_a)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)