'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/9 21:31       
@Author:ZHANG               
 
'''
import sys


# It also can use tuple to compare the continues number
def main(lines):
    S = lines[0]
    T = lines[1]
    i, j = 0, 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        elif i > 1 and S[i-1] == T[j] and S[i-1] == S[i-2]:
            j += 1
        else:
            print("No")
            return
    if i > 1 and S[i-1] == S[i-2]:
        while j < len(T):
            if T[j] == S[i-1]:
                j += 1
            else:
                break

    if j == len(T):
        print('Yes')
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)