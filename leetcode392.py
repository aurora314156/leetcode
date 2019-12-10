"""
*     
"""
class Solution:
    def isSubsequence(self, S: str, t: str) -> bool:
        Dict, string_len, res = dict(), len(S), []
        start, end = 0, 0
        for i in range(string_len):
            Dict[S[i]] = i
        for i in range(string_len):
            end = max(end, Dict[S[i]])
            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res