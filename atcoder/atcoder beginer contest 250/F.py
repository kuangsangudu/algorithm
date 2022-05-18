'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/10 16:16       
@Author:ZHANG               
 
'''

import math
import os
import random
import re
import sys
import collections


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N = int(lines[0])
    C = map(int, lines[1].split(" "))
    C_count = collections.Counter(C)
    Mod = 100003
    v = 1
    for key, val in C_count.items():
        v = (v * math.factorial(val)) % Mod
    ret = v
    sorted_key = sorted(C_count.keys())
    lens = len(sorted_key)
    for i, key in enumerate(sorted_key):
        if i == len(sorted_key)-1:
            continue
        # inchange = math.factorial(C_count[key]-1)
        # othechange = v // math.factorial(C_count[key])
        # ret = (ret + (lens-i-1) * C_count[key] * othechange * inchange) % Mod
        ret = (ret + (lens - i - 1) * C_count[key] * v) % Mod
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
