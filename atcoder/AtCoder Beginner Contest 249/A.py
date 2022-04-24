'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 20:36       
@Author:ZHANG               
 
'''

import sys


def main(lines):
    A, B, C, D, E, F, X = list(map(int, lines[0].split()))
    Takahashi_dis = X//(A+C) * (A*B) + min(X%(A+C), A) * B
    Aoki_dis = X//(D+F) * (D*E) + min(X%(D+F), D) * E
    # print(Takahashi_dis, Aoki_dis, X//(B+C), min(X%(B+C), B))
    if Takahashi_dis > Aoki_dis:
        print("Takahashi")
    elif Takahashi_dis < Aoki_dis:
        print("Aoki")
    else:
        print("Draw")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
