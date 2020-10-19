class Solution():
    def decodeString(self, s):
        ans, cur_num = '', 0
        stack = []
        for char in s:
            if char == '[':
                stack.append(ans)
                stack.append(cur_num)
                ans = ''
                cur_num = 0
            elif char == ']':
                pre_nums = stack.pop()
                pre_string = stack.pop()
                ans = pre_string + pre_nums * ans
            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)
            else:
                ans += char
        return ans