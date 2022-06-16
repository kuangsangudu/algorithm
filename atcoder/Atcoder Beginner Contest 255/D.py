'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/11 21:34       
@Author:ZHANG               
 
'''
import sys


def main(lines):
    X, Q = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    A.sort()
    sums = [0]
    for num in A:
        sums.append(sums[-1] + num)
    for line in lines[2:]:
        x = int(line)
        l, r = 0, len(A)-1
        while l < r:
            mid = l + (r-l)//2
            if A[mid] < x:
                l = mid + 1
            else:
                r = mid
        if A[l] > x:
            l -= 1

        if l < 0:
            left = 0
            right = sums[-1] - len(A) * x
        else:
            left = (l+1)*x - sums[l+1] if l >= 0 else 0
            right = sums[-1] - sums[l+1] - (len(A)-l-1) * x if l < len(A)-1 else 0

        print(left + right)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)