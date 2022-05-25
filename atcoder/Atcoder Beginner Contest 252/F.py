'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/22 1:54       
@Author:ZHANG               
 
'''
import heapq
import sys


# this problem is a bit like Huffman Coding(Tree)
def main(lines):
    N, L = map(int, lines[0].split(" "))
    A = list(map(int, lines[1].split(" ")))
    re = []
    for num in A:
        L -= num
        heapq.heappush(re, num)
    if L > 0:
        # when L is larger than the sum of array A, we need to put it into the heapq.
        heapq.heappush(re, L)
    ret = 0
    while len(re) > 1:
        n1 = heapq.heappop(re)
        n2 = heapq.heappop(re)
        ret += n1 + n2
        heapq.heappush(re, n1+n2)

    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
