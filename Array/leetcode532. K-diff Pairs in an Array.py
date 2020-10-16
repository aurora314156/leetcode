class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, v in count.items():
                if v >= 2:
                    res += 1
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
        return res