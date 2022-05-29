'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/28 21:02       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    H, W = map(int, lines[0].split(" "))
    S = lines[1:]
    O_place = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                O_place.append([i, j])
    print(abs(O_place[0][0] - O_place[1][0]) + abs(O_place[0][1] - O_place[1][1]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
