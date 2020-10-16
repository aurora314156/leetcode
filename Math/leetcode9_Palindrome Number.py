class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x % 10 is 0 and x > 0) or x < 0: return False
        p_num, tmp_x = 0, x
        while tmp_x > 0:
            p_num = p_num * 10 + tmp_x % 10
            tmp_x //= 10
            
        return True if x == p_num else False