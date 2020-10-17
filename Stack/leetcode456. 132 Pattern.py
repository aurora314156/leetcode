# [2, 4, 2, 3, 5]
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        s = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third: return True
            while s and nums[i] > s[-1]:
                third = s[-1]
                s.pop()
            s.append(nums[i])
        return False