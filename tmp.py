"""
Des: 350. Intersection of Two Arrays II
Tags: Binary search, DP ,Greedy
"""
class Solution:
    def isSubsequence(self, s, t):
        tmp = 0
        for ss in s:
            tmp = t.find(ss, tmp) + 1
            if tmp == 0:
                return False
        return True
            
if __name__ == '__main__':
    s, t =  "acb", "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(res)