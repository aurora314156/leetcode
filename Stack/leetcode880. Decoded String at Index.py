"""
Des: 880. Decoded String at Index
Tags: Stack
"""

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        maxLen = 0
        for i, c in enumerate(S):
            maxLen = maxLen * int(c) if c.isdigit() else maxLen + 1
            if K <= maxLen: break
        for j in range(i, -1, -1):
            char = S[j]
            if char.isdigit():
                maxLen /= int(char)
                K %= maxLen
            else:
                if K == maxLen or not K: return char
                maxLen -= 1
