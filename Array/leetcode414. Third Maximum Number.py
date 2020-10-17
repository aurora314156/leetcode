class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif first > num and num > second:
                second, third = num, second
            elif num < second and num > third:
                third = num
        return third if third != float('-inf') else first