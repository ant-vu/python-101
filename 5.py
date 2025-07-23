class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time: O(n^2), space: O(n^2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        i, j = ans
        return s[i : j + 1]

        # time: O(n^3), space: O(1)
        # for i in range(len(s), 0, -1):
        #     for j in range(len(s) - i + 1):
        #         if s[j:j+i] == s[j:j+i][::-1]:
        #             return s[j:j+i]