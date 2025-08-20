class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # time: O(n^2), space: O(n)
        dp, dpPrev = [0] * len(s), [0] * len(s)
        for l in range(len(s) - 1, -1, -1):
            dp[l] = 1
            for r in range(l + 1, len(s)):
                if s[l] == s[r]:
                    dp[r] = dpPrev[r - 1] + 2
                else:
                    dp[r] = max(dpPrev[r], dp[r - 1])
            dp, dpPrev = [0] * len(s), dp
        return dpPrev[len(s) - 1]

        # time: O(n^2), space: O(n^2)
        # dp = [[0] * len(s) for _ in range(len(s))]
        # for l in range(len(s) - 1, -1, -1):
        #     dp[l][l] = 1
        #     for r in range(l + 1, len(s)):
        #         if s[l] == s[r]:
        #             dp[l][r] = dp[l + 1][r - 1] + 2
        #         else:
        #             dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        # return dp[0][len(s) - 1]

        # time: O(n^2), space: O(n^2)
        # @cache
        # def dp(l, r):
        #     if l > r:
        #         return 0
        #     elif l == r:
        #         return 1
        #     elif s[l] == s[r]:
        #         return dp(l + 1, r - 1) + 2
        #     return max(dp(l, r - 1), dp(l + 1, r))
        # return dp(0, len(s) - 1)