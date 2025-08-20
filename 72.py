class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # time: O(m*n), space: O(m*n)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]

        # time: O(m*n), space: O(m*n)
        # def helper(word1, word2, i, j, memo):
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #     elif i == len(word1):
        #         return len(word2) - j
        #     elif j == len(word2):
        #         return len(word1) - i
        #     elif (i, j) not in memo:
        #         if word1[i] == word2[j]:
        #             res = helper(word1, word2, i + 1, j + 1, memo)
        #         else:
        #             insert = 1 + helper(word1, word2, i, j + 1, memo)
        #             delete = 1 + helper(word1, word2, i + 1, j, memo)
        #             replace = 1 + helper(word1, word2, i + 1, j + 1, memo)
        #             res = min(insert, delete, replace)
        #         memo[(i, j)] = res
        #     return memo[(i, j)]
        # return helper(word1, word2, 0, 0, {})

        # time: O(3^(m+n)), space: O(m+n), TLE
        # if not word1 and not word2:
        #     return 0
        # elif not word1:
        #     return len(word2)
        # elif not word2:
        #     return len(word1)
        # elif word1[0] == word2[0]:
        #     return self.minDistance(word1[1:], word2[1:])
        # insert = 1 + self.minDistance(word1, word2[1:])
        # delete = 1 + self.minDistance(word1[1:], word2)
        # replace = 1 + self.minDistance(word1[1:], word2[1:])
        # return min(insert, delete, replace)