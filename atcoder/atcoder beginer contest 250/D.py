'''
@Project: algorithm   
@Description: TODO          
@Time:2022/5/8 21:48       
@Author:ZHANG               
 
'''
import sys
import math

class oula:
    def __init__(self, N):
        self.N = N
        self.isprime = [True] * self.N
        self.isprime[0] = False
        self.isprime[1] = False
        self.prime = []
        self.__init()

    def __init(self):
        cnt = 0
        for i in range(2, self.N):
            if self.isprime[i]:
                self.prime.append(i)
                cnt += 1
            for j in range(cnt):
                if i * self.prime[j] >= self.N:
                    break
                self.isprime[i * self.prime[j]] = False
                if i % self.prime[j] == 0:
                    break

    def judge(self, n):
        return self.isprime[n]

    def get_nthprime(self, n):
        return self.prime[n]


def main(lines):
    N = int(lines[0])
    if N == 1:
        print(0)
        return
    oul = oula(math.ceil(N**(1/3))).prime
    ret = 0
    for i, n in enumerate(oul):
        for j in range(i+1, len(oul)):
            if n * oul[j]**3 <= N:
                ret += 1
            else:
                break
    print(ret)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)