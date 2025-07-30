class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # time: O(n^2), space: O(n^2)
        t = s[::-1]
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return dp[-1][-1]