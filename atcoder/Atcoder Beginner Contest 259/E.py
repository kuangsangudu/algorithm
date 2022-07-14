'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/9 22:56       
@Author:ZHANG               
 
'''
import collections
import sys


def main(lines):
    N = int(lines[0])
    m = collections.defaultdict(list)
    re = []
    for line in lines[1:]:
        line = list(map(int, line.split(" ")))
        if len(line) == 1:
            re.append([])
        else:
            re[-1].append(line)
            if m.get(line[0], -1) != -1:
                if line[1] >= m[line[0]][0]:
                    m[line[0]][0], m[line[0]][1] = line[1], m[line[0]][0]
                elif line[1] > m[line[0]][1]:
                    m[line[0]][1] = line[1]
            else:
                m[line[0]] = [line[1], 0]

    visited = set()
    for line in re:
        sums = []
        for p, o in line:
            if o == m[p][0] and o > m[p][1]:
                sums.append((p, o-m[p][1]))
        visited.add(tuple(sums))
    print(len(visited))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)