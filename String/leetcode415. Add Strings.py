class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry_plus = 0
        minstrl = min(len(num1), len(num2))
        maxstr = num1 if len(num1)>len(num2) else num2
        
        for i in range(len(maxstr)):
            if i < minstrl:
                cur_sum = int(num1[i]) + int(num2[i]) + carry_plus
            else:
                cur_sum = int(maxstr[i]) + carry_plus
            carry_plus = cur_sum // 10
            cur_sum %= 10
            s += str(cur_sum)
            
        s += str(carry_plus)
        if s[len(s)-1] == "0":
            s = s[:-1]
        return s[::-1]