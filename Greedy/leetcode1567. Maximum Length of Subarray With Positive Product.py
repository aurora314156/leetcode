class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, ans = 0, 0, 0
        for num in nums:
            if num > 0:
                pos += 1
                if neg:
                    neg += 1
                ans = max(pos, ans)
            elif num < 0:
                pos, neg = neg, pos
                neg += 1
                if pos:
                    pos += 1
                ans = max(pos, ans)
            else:
                pos = neg = 0
        return ans
            