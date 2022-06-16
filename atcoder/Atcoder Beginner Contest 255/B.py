'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/11 21:03       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    N, K = map(int, lines[0].split(" "))
    A = set(map(int, lines[1].split(" ")))
    person = []
    for line in lines[2:]:
        x, y = map(int, line.split(" "))
        person.append([x, y])
    mins = [float("inf")] * N

    for num in A:
        for j in range(N):
            mins[j] = min(mins[j], (person[num-1][0]-person[j][0])**2 + (person[num-1][1]-person[j][1])**2)
    print(max(mins)**0.5)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)