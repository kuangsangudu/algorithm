'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/15 14:29       
@Author:ZHANG               

'''
import sys


def f(a):
    ret, s = 0, 0
    for x in a:
        if x == 0:
            ret += s * (s + 1) // 2
            s = 0
        else:
            s += 1
    ret += s * (s + 1) // 2
    return ret

# all_combine means all the situations, n_x means not contain X, n_y means not contain y,
# n_xoy means not contain x nor y   the set containing x and y is what we want


def main(lines):
    N, X, Y = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    all_combine, n_x, n_y, n_xoy = [1] * N, [1] * N, [1] * N, [1] * N
    for i in range(N):
        # exclude the boundary value
        if arr[i] < Y or arr[i] > X:
            all_combine[i], n_x[i], n_y[i], n_xoy[i] = 0, 0, 0, 0
        if arr[i] == X:
            n_x[i], n_xoy[i] = 0, 0
        if arr[i] == Y:
            n_y[i], n_xoy[i] = 0, 0
    print(f(all_combine) - f(n_x) - f(n_y) + f(n_xoy))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
