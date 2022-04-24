'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/23 20:36
@Author:ZHANG

'''

import sys


def main(lines):
    S = lines[0]
    visited = set()
    is_U, is_D, is_pairs = False, False, False
    for i, n in enumerate(S):
        if n in visited:
            is_pairs = True
        visited.add(n)
        if n.islower():
            is_D = True
        if n.isupper():
            is_U = True
    if is_D and is_U and not is_pairs:
        print("Yes")
    else:
        print('No')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
