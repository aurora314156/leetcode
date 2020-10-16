class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative_ans = False if dividend * divisor >= 0 else True
        dividend, divisor, ans = abs(dividend), abs(divisor), 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
            
        if negative_ans:
            ans *= -1

        return min(max(-2147483648, ans), 2147483647)