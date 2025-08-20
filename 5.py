class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time: O(n^2), space: O(1)
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1
        res = [0, 0]
        for i in range(len(s)):
            oddLen = expand(i, i)
            if oddLen > res[1] - res[0] + 1:
                dist = oddLen // 2
                res = [i - dist, i + dist]
            evenLen = expand(i, i + 1)
            if evenLen > res[1] - res[0] + 1:
                dist = (evenLen // 2) - 1
                res = [i - dist, i + dist + 1]
        return s[res[0]:res[1]+1]

        # time: O(n^2), space: O(n^2)
        # dp = [[False] * len(s) for _ in range(len(s))]
        # res = [0, 0]
        # for i in range(len(s)):
        #     dp[i][i] = True
        # for i in range(len(s) - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         res = [i, i + 1]
        # for diff in range(2, len(s)):
        #     for i in range(len(s) - diff):
        #         j = i + diff
        #         if s[i] == s[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             res = [i, j]
        # return s[res[0]:res[1]+1]

        # time: O(n^3), space: O(n)
        # for i in range(len(s), -1, -1):
        #     for j in range(len(s) - i):
        #         if s[j:j+i+1] == s[j:j+i+1][::-1]:
        #             return s[j:j+i+1]