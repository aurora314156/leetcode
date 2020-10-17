class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         self.dfs(nums, 0, res, [])
#         return res
#     def dfs(self, nums, index, res, path):
#         res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, i + 1, res, path + [nums[i]])
    def subsets(self, nums):    
        # n = len(nums)
        # return [[nums[i] for i in range(n) if s & 1 << i > 0] for s in range(1 << n)]
        res = [[]]
        for num in nums:
            print(res)
            res += [item+[num] for item in res]
            print(res)
        return res
        