import math
"""
Des: majority number
Algo: boyer-moore voting algorithm
"""
class Solution:
    def majorityElement(self, nums):
        num1, count1 = None, 0
        num2, count2 = None, 0
        for x in nums:
            if x == num1:
                count1 += 1
            elif x == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = x, 1
            elif count2 == 0:
                num2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1
        print(num1)
        print(num2)
        count1, count2 = 0,0
        for x in nums:
            if x == num1:
                count1 += 1
            if x == num2:
                count2 += 1
        res = []
        if count1 > math.ceil(len(nums) / 3.0):
            res.append(num1)
        if count2 > math.ceil(len(nums) / 3.0):
            res.append(num2)
        return res

nums = [1,1,1,3,3,2,2]
s = Solution().majorityElement(nums)
print(s)