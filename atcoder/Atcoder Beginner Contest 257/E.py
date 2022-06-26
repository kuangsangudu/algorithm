'''
@Project: algorithm   
@Description: TODO          
@Time:2022/6/25 22:51       
@Author:ZHANG               
 
'''
import collections
import sys


#
def main(lines):
    N = int(lines[0])
    C = list(map(int, lines[1].split(" ")))
    re = collections.defaultdict(int)
    dp = [0] * (N+1)
    for i, num in enumerate(C, start=1):
        re[num] = i
    keys = sorted(re.keys())
    for key, value in re.items():
        dp[key] = value
    for i in range(1, N+1):
        if dp[i]:
            for k in keys:
                if i + k > N:
                    break
                dp[i+k] = max(dp[i+k], dp[i]*10 + re[k])
    print(max(dp))


def main1(lines):
    N = int(lines[0])
    C = list(map(int, lines[1].split(" ")))
    mins = min(C)
    minsidx = -1
    for i in range(len(C)-1, -1, -1):
        if C[i] == mins:
            minsidx = i
            t, r = divmod(N, mins)
            break

    if t == 0:
        print(0)
        return

    ret = t * [str(minsidx+1)]
    for i in range(t):
        for j in range(8, minsidx, -1):
            if r >= C[j]-mins:
                ret[i] = str(j+1)
                r -= (C[j]-mins)
                break
        if ret[i] == str(minsidx+1):
            break
    print("".join(ret))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)
