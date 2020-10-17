class Solution:
    def climbStairs(self, n: int) -> int:
        m = [1, 2]
        if n == 1: return m[0]
        for i in range(2, n+1):
            m.append(m[i-1] + m[i-2])
        return m[n-1]