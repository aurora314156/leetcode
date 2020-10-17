class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        slow = fast = 0
        while fast < l:
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1