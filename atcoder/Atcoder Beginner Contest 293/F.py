'''
@Project: algorithm   
@Description: TODO          
@Time:2023/3/16 23:47       
@Author:ZHANG               
 
'''


import bisect
import collections
import copy
import fractions
import functools
import itertools
import math
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


# nums是test样例， inp是2进制表示值
def judge(nums, inp):
    def f(num):
        ret = 0
        d = 1
        for i in a:
            ret += i * d
            d *= num
        return ret

    a = []
    while inp:
        a.append(inp % 2)
        inp >>= 1
    l, r = 2, nums
    while l <= r:
        mid = (l+r)//2
        re = f(mid)
        if re < nums:
            l = mid + 1
        elif re == nums:
            return True
        else:
            r = mid - 1
    return False


def main(lines):
    line = list(map(int, lines))
    for t in line[1:]:
        ret = 0
        # 判断结果数大于10000的b
        for b in range(2, int(pow(t, 0.25))+1):
            n = t
            flag = True
            while n:
                if n % b > 1:
                    flag = False
                    break
                else:
                    n //= b
            ret += flag

        # 判断结果数小于1111的b值
        for x in range(2, 16):
            ret += judge(t, x)
        print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)