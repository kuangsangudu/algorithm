'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/2 20:30       
@Author:ZHANG               
 
'''

import heapq
import math
import sys


def main(lines):
    K = int(lines[0])
    hour, minute = str(21 + K // 60), str(K % 60)
    if len(minute) == 1:
        minute = "0" + minute
    print(hour + ":" + minute)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)