'''
@Project: algorithm
@Description: TODO
@Time:2022/7/6 0:07
@Author:ZHANG

'''
import sys


def square(b, k, x, y):
    xn, yn = x // b, y // b
    x0, x1, y0, y1 = xn * b, (xn + 1) * b, yn * b, (yn + 1) * b
    res = [
            [x, y0, (y - y0) * k],
            [x, y1, (y1 - y) * k],
            [x0, y, (x - x0) * k],
            [x1, y, (x1 - x) * k]
        ]
    return res


def main(lines):
    T = lines[0]
    for line in lines[1:]:
        B, K, Sx, Sy, Gx, Gy = map(int, line.split(" "))
        s_points = square(B, K, Sx, Sy)
        g_points = square(B, K, Gx, Gy)
        ret = (abs(Sx-Gx) + abs(Sy-Gy)) * K
        for i in range(4):
            xi, yi, di = s_points[i]
            for j in range(4):
                xj, yj, dj = g_points[j]
                tmp = di + dj
                if i < 2 and j < 2 and xi // B == xj // B and yi != yj:
                    x0, x1 = s_points[2][0], s_points[3][0]
                    tmp += min(xi + xj - x0 * 2, x1 * 2 - xi - xj) + abs(yj - yi)
                elif i >= 2 and j >= 2 and yi // B == yj // B and xi != xj:
                    y0, y1 = s_points[0][1], s_points[1][1]
                    tmp += min(yi + yj - y0 * 2, y1 * 2 - yi - yj) + abs(xj - xi)
                else:
                    tmp += abs(xj - xi) + abs(yj - yi)
                ret = min(ret, tmp)
        print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
