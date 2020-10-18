class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        if num == 1: return True
        while l < r:
            m = l + (r - l) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 < num:
                l = m + 1
            else:
                r = m
        return False