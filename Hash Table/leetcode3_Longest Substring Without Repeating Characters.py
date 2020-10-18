class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, ans, j = {}, 0, -1
        for i, v in enumerate(s):
            if v in d and d[v] > j:
                j = d[v]
            d[v] = i
            ans = max(ans, i - j)
        return ans