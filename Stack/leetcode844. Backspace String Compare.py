class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getStr(Str):
            stack = []
            for ss in Str:
                if ss != "#":
                    stack.append(ss)
                elif stack:
                    stack.pop()
            return stack
        return getStr(S) == getStr(T)
    