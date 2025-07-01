class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time: O(m * n), space: O(m * n)
        dp = [[1] * n] * m
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]