class Solution:
    def isHappy(self, n: int) -> bool:
        dnum, s = 0, set()
        while n != 1 and n not in s:
            s.add(n)
            dnum = 0
            while n:
                dnum += (n%10) ** 2
                n //= 10
            n = dnum
            
        return n == 1