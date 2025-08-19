class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time: O(m * n), space: O(n)
        dp = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]

        # time: O(m * n), space: O(n)
        # dp = [[1] * n for _ in range(2)]
        # for _ in range(m - 1):
        #     for c in range(1, n):
        #         dp[0][c] = dp[1][c]
        #         dp[1][c] += dp[1][c - 1]
        # return dp[-1][-1]

        # time: O(m * n), space: O(m * n)
        # dp = [[1] * n for _ in range(m)]
        # for r in range(1, m):
        #     for c in range(1, n):
        #         dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        # return dp[-1][-1]