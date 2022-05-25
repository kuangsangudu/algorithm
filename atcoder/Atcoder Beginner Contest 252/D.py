'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/21 21:28       
@Author:ZHANG               
 
'''
import collections
import sys


def main(lines):
    N = int(lines[0])
    A = list(map(int, lines[1].split(" ")))
    re = collections.defaultdict(int)
    for num in A:
        re[num] += 1
    ret = 0
    rr = [0]

    keys = sorted(re.keys())
    for key in keys:
        rr.append(rr[-1] + re[key]*(re[key]-1)//2)
    lens = len(A)
    sums = 0
    for i, key in enumerate(keys[:-2]):
        sums += re[key]
        ret += re[key] * ((lens-sums) * (lens-sums-1)//2 - (rr[-1] - rr[i+1]))
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)