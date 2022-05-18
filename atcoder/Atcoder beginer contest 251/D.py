'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/14 21:20       
@Author:ZHANG               
 
'''
import sys


def main1(lines):
    W = int(lines[0])
    ret = []
    re = [False] * (W+1)
    for i in range(1, W+1):
        if re[i]:
            continue
        re[i] = True
        for j in range(len(ret)):
            if i+ret[j] > W:
                break
            re[i+ret[j]] = True
            for w in range(j+1, len(ret)):
                if i+ret[j]+ret[w] > W:
                    break
                re[i+ret[j]+ret[w]] = True
        ret.append(i)
    print(len(ret))
    print(" ".join(list(map(str, ret))))


# just build 300 numbers directly
def main(lines):
    W = int(lines[0])
    ret = [i for i in range(1, 101)]
    ret += [i * 100 for i in range(1, 101)]
    ret += [i * 10000 for i in range(1, 101)]

    print(300)
    print(*ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
