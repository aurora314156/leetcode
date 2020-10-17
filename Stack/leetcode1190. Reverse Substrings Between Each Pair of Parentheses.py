class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ''
        for c in s:
            if c == ")":
                tmp_l = []
                while stack[-1] != "(":
                    tmp_l.append(stack.pop())
                stack.pop()
                for ll in tmp_l:
                    stack.append(ll)
            else:
                stack.append(c)
        res = res.join(stack)
        return res