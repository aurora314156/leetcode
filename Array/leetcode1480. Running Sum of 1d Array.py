class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums
        for n in range(1, len(nums)):
            nums[n] += nums[n-1]
        return nums