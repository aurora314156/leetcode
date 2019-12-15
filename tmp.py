"""
Des: 880. Decoded String at Index
Tags: Stack
"""

import pysnooper
class Solution:
    @pysnooper.snoop()
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
            

if __name__ == '__main__':
    #S, K = "leet2code3", 10
    S, K = "ha22", 5
    #S, K = "czjkk9elaqwiz7s6kgvl4gjixan3ky7jfdg3kyop3husw3fm289thisef8blt7a7zr5v5lhxqpntenvxnmlq7l34ay3jaayikjps", 768077956
    #S, K = "a2345678999999999999999", 1
    res = Solution().decodeAtIndex(S, K)
    
   