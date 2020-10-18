class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = None, 0
        for e in nums:
            if e == num:
                count += 1
            elif count == 0:
                num = e
                count = 1
            else:
                count -= 1
        return num
