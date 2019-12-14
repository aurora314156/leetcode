"""
Des: 880. Decoded String at Index
Tags: Stack
"""

import pysnooper
class Solution:
    @pysnooper.snoop()
    def decodeAtIndex(self, S: str, K: int) -> str:
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1
        # tmpStr, curMaxLen = "", 1
        # for char in S:
        #     if char.isdigit(): 
        #         tmpStr *= int(char)

        #     else:
        #         tmpStr += char
        #     curMaxLen = len(tmpStr)
        #     if curMaxLen >= K:
        #         return tmpStr[ (K % len(tmpStr))-1]
            
#


if __name__ == '__main__':
    S, K = "leet2code3", 10
    #S, K = "czjkk9elaqwiz7s6kgvl4gjixan3ky7jfdg3kyop3husw3fm289thisef8blt7a7zr5v5lhxqpntenvxnmlq7l34ay3jaayikjps", 768077956
    #S, K = "a2345678999999999999999", 1
    res = Solution().decodeAtIndex(S, K)
    
    