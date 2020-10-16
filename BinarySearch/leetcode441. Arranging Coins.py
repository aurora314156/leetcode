class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1