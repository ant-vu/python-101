class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # time: O(m*n), space: O(m*n)
        @cache
        def dp(i, j):
            if i == -1 or j == -1:
                return j == -1
            return dp(i - 1, j) + (s[i] == t[j]) * dp(i - 1, j - 1)
        return dp(len(s) - 1, len(t) - 1)