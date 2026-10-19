class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        vec = []
        for i in range(left,right+1):
            n = i
            con = True
            while n>0:
                rem = n % 10
                if rem == 0 or i % rem != 0:
                    con = False
                    break
                n //= 10
            if con:
                vec.append(i)
        return vec