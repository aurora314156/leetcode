class Solution:
    def maxPower(self, s: str) -> int:
        prev, maxL, curL = "", 0, 0
        for char in s:
            if prev == char:
                curL += 1
            else:
                curL = 1
                prev = char

            maxL = max(maxL, curL)
        return maxL