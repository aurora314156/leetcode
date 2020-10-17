class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)+1
        n = len(B)+1
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]