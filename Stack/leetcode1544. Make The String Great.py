class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for char in s:
            if ans and abs(ord(ans[-1]) - ord(char)) == 32:
                ans.pop()
            else:
                ans.append(char)
        return "".join(ans)