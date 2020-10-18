class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower(nums, target)
        right = self.upper(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    def lower(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
    def upper(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return l