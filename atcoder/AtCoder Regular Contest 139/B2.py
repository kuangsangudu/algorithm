'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/26 15:51       
@Author:ZHANG               
 
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections
import math


def factor(n, Mod):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s % Mod


def comb(n, m, Mod):
    return (math.factorial(n)//(math.factorial(n-m)*math.factorial(m))) % Mod


def solution(S):
    # write your code in Python 3.6
    vowels_num, consonants_num = 0, 0
    vowels = "AEIOU"
    v, c = collections.defaultdict(int), collections.defaultdict(int)
    Mod = 10 ** 9 + 7
    for i in S:
        if i in vowels:
            v[i] += 1
            vowels_num += 1
        else:
            c[i] += 1
            consonants_num += 1
    if consonants_num == vowels_num + 1 or consonants_num == vowels_num:
        ret = 1
        for val in v.values():
            ret = ret * comb(vowels_num, val, Mod) % Mod
            vowels_num -= val
        for val in c.values():
            ret = ret * comb(consonants_num, val, Mod) % Mod
            consonants_num -= val
        return ret
    else:
        return 0


print(solution('AABCY'))
