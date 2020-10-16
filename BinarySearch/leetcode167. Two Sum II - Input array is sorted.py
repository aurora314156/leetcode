class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)
        for ind in range(r):
            goal = target - numbers[ind]
            l = 0
            while l < r:
                m = l + (r - l) // 2
                if numbers[m] == goal:
                    return [ind+1, m+1]
                if numbers[m] < goal:
                    l = m + 1
                else:
                    r = m