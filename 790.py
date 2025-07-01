class Solution:
    def numTilings(self, n: int) -> int:
        # time: O(n), space: O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        mod = 10 ** 9 + 7
        dp = [1, 1, 2, 5] + [0] * (n - 3)
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod
        return dp[n]