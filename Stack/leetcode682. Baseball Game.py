class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for o in ops:
            if o == "C":
                ans.pop()
            elif o == "D":
                ans.append(int(ans[-1])*2)
            elif o == "+":
                ans.append(int(ans[-1]) + int(ans[-2]))
            else:
                ans.append(int(o))
        return sum(ans)