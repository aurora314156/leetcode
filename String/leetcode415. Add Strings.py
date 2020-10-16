class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j  = len(num1)-1, len(num2)-1
        res = ''
        c = 0
        while i > -1 or j > -1:
            if i > -1:
                c += ord(num1[i]) - ord('0')
            if j > -1:
                c += ord(num2[j]) - ord('0')
            res += chr(c % 10 + ord('0'))
            c //= 10
            i -= 1
            j -= 1
        if c == 1:
            res += '1'
        return res[::-1]