class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return r
        # i = bisect.bisect_left(nums, target)
        # return i