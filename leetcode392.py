"""
Des: 392. Is Subsequence
Tags: Binary search, DP ,Greedy
""" 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tmp = 0
        for ss in s:
            tmp = t.find(ss, tmp) + 1
            if tmp == 0:
                return False
        return True

