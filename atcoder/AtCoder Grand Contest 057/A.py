'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/7 20:54       
@Author:ZHANG               
 
'''
# https://atcoder.jp/contests/agc057/editorial/3923
# the f function is the import thing, use binary search find the point.
import sys


def f(x: int):
    return min(10*x, x+(10**len(str(x))))


def main(lines):
    T = lines[0]
    for line in lines[1:]:
        l, r = map(int, line.split(" "))
        maxs = r
        while l < r:
            mid = l + (r-l)//2
            if f(mid) <= maxs:
                l = mid + 1
            else:
                r = mid
        print(maxs-l+1)


# wrong method
# def xunzhao(num):
#     sn = str(num)
#     lens = len(sn)
#     if lens == 1:
#         return num
#     else:
#         retr = 10 ** (lens - 2) * 9 + num - (10 ** (lens - 1) - 1)
#         if sn[0] != "1":
#             retr -= 10 ** (lens - 2) * 9
#         else:
#             retr -= max(num-(10 ** (lens - 1))-(10 ** (lens - 2) - 1), int(sn[:-1]) - (10 ** (lens - 2) - 1))
#     return retr
#
#
# def main(lines):
#     T = lines[0]
#     for line in lines[1:]:
#         l, r = map(int, line.split(" "))
#         if len(str(r)) <= len(str(l))+1:
#             print(xunzhao(r-l+1))
#         else:
#             print(xunzhao(r))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
