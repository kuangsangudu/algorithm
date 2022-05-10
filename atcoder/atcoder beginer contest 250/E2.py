'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/10 22:50       
@Author:ZHANG               
 
'''
import sys


def get_lenanddiff(a):
    temp = set()
    N = len(a)
    a_length, a_diff = [0] * (N + 1), []
    for i, n in enumerate(a, start=1):
        if n not in temp:
            temp.add(n)
            a_diff.append(n)
        a_length[i] = len(temp)
    temp.clear()
    return a_length, a_diff


def main(lines):
    N = int(lines[0])
    a = list(map(int, lines[1].split(" ")))
    b = list(map(int, lines[2].split(' ')))
    Q = int(lines[3])
    a_length, a_diff = get_lenanddiff(a)
    b_length, b_diff = get_lenanddiff(b)

    temp = set()
    C = [False] * (N + 1)
    for n, (i, j) in enumerate(zip(a_diff, b_diff), start=1):
        if i in temp:
            temp.remove(i)
        else:
            temp.add(i)
        if j in temp:
            temp.remove(j)
        else:
            temp.add(j)
        C[n] = len(temp) == 0

    for X in lines[4:]:
        x, y = map(int, X.split(' '))
        if a_length[x] == b_length[y] and C[a_length[x]]:
            print("Yes")
        else:
            print('No')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
