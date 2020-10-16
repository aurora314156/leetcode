class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, d = -1, {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for k, v in d.items():
            if v is 1:
                ans = k
        return ans