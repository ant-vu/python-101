class Solution:
    def numSquares(self, n: int) -> int:
        # time: O(n * sqrt(n)), space: O(n)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            minVal = inf
            j = 1
            while j * j <= i:
                minVal = min(minVal, dp[i - j * j] + 1)
                j += 1
            dp[i] = minVal
        return dp[n]