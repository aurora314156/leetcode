class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i, v in enumerate(nums, 0):
            if v is not val:
                nums[j] = v
                j+=1
        return j