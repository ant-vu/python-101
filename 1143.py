class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time: O(m * n), space: O(min(m, n))
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        dp = [0] * len(text1)
        longest = 0
        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)
        return longest

        # time: O(m * n), space: O(m * n)
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         if text1[i] == text2[j]:
        #             dp[i + 1][j + 1] = 1 + dp[i][j]
        #         else:
        #             dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        # return dp[-1][-1]