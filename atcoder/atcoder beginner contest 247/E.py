'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/14 23:46
@Author:ZHANG

'''
import collections
import sys


def process(nums, X, Y):
    i, j = 0, 0
    mins, maxs = 0, 0
    ret = 0
    while i < len(nums):
        while j < len(nums) and (mins == 0 or maxs == 0):
            if nums[j] == X:
                maxs += 1
            if nums[j] == Y:
                mins += 1
            j += 1
        if maxs and mins:
            ret += len(nums)-j+1
        if nums[i] == X:
            maxs -= 1
        if nums[i] == Y:
            mins -= 1
        i += 1
    return ret


def main(lines):
    N, X, Y = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    i = 0
    nums = []
    ret = 0
    while i < len(arr):
        if arr[i] > X or arr[i] < Y:
            ret += process(nums, X, Y)
            nums = []
        else:
            nums.append(arr[i])
        i += 1
    if nums:
        ret += process(nums, X, Y)
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
