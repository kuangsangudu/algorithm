'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 21:27
@Author:ZHANG

'''
import collections
import sys


def main(lines):
    N = int(lines[0])
    arr = list(map(int, lines[1].split(" ")))
    re = collections.Counter(arr)
    keys = list(re.keys())
    keys.sort()
    ret = 0
    maxs = keys[-1]
    for i in keys:
        for j in keys:
            if i * j > maxs:
                break
            if re.get(i*j, -1) != -1:
                ret += re[i] * re[j] * re[i*j]
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
