'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/14 23:46
@Author:ZHANG

'''
import collections
import sys


def main(lines):
    N = int(lines[0])
    re = collections.deque([])
    for i, line in enumerate(lines[1:]):
        r = [int(j) for j in line.split(" ")]
        if len(r) == 3:
            if re and re[-1][0] == r[1]:
                re[-1][1] += r[2]
            else:
                re.append([r[1], r[2]])
        else:
            ret = 0
            plus = r[1]
            while plus:
                if re[0][1] <= plus:
                    ret += re[0][0] * re[0][1]
                    plus -= re[0][1]
                    re.popleft()
                else:
                    ret += re[0][0] * plus
                    re[0][1] -= plus
                    break
            print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
