class Solution:
    def freqAlphabets(self, s):
        ans, i ="", 0
        step=len(s)
        while i < step:
            if i + 2 < step and s[i + 2] == '#':
                ans += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                ans += chr(int(s[i]) + 96)
                i += 1
        return ans