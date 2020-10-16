#  001110010    prev = 0    cur = 0
#  0 01110010    prev = 0    cur = 1
# 0 0 1110010    prev = 0    cur = 2
# 00 1 110010    prev = 2    cur = 1    01
# 001 1 10010    prev = 2    cur = 2    0011
# 0011 1 0010    prev = 2    cur = 3
# 00111 0 010    prev = 3    cur = 1    10
# 001110 0 10    prev = 3    cur = 2    1100
# 0011100 1 0    prev = 2    cur = 1    01
# 00111001 0     prev = 1    cur = 1    10
# https://www.polarxiong.com/archives/LeetCode-696-count-binary-substrings.html

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevlen, curlen, ans = 0, 0, 0    
        for i in range(len(s)):
            if s[i] == s[i-1]:
                curlen += 1
            else:
                prevlen = curlen
                curlen = 1
            if prevlen >= curlen:
                ans += 1
        return ans