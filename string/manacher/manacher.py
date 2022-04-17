'''
@Project: algorithm   
@Description: TODO          
@Time:2022/04/16 11:43       
@Author:ZHANG               
 
'''


class manacher:
    @staticmethod
    def trans(s):
        ret = ["#"] * (len(s)*2+1)
        for i, n in enumerate(s):
            ret[2*i+1] = n
        return ret

    def manacher(self, s):
        new_s = self.trans(s)
        lens = len(new_s)
        c, r = -1, -1
        i = 0
        re = [0] * lens
        ret = 1
        while i < lens:
            # original idea
            # if i > c+r:
            #     i_r = 1
            #     while i-i_r >= 0 and i+i_r < lens and new_s[i-i_r] == new_s[i+i_r]:
            #         i_r += 1
            #     re[i] = i_r-1
            #     c, r = i, i_r-1
            # else:
            #     ti = c - (i - c)
            #     if ti-re[ti] > c-r:
            #         re[i] = re[ti]
            #     elif ti-re[ti] < c-r:
            #         re[i] = ti - (c-r)
            #     else:
            #         i_r = ti - (c-r)+1
            #         while i - i_r >= 0 and i + i_r < lens and new_s[i - i_r] == new_s[i + i_r]:
            #             i_r += 1
            #         re[i] = i_r-1
            #         c, r = i, i_r-1
            # i += 1

            # optimization
            i_r = 1 if i > c+r else min(re[2*c-i], c-i+r) + 1
            while i - i_r >= 0 and i + i_r < lens and new_s[i - i_r] == new_s[i + i_r]:
                i_r += 1
            i_r -= 1
            re[i] = i_r
            ret = max(ret, i_r)
            if i_r + i > c + r:
                c, r = i, i_r
            i += 1
        return ret
