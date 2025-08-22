class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(m * n), space: O(n)
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        dpPrev = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]
        return dp[-1]

        # time: O(m * n), space: O(m * n)
        # m, n = len(nums1), len(nums2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if nums1[i - 1] == nums2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        # return dp[-1][-1]

        # time: O(m * n), space: O(m * n)
        # def solve(i, j):
        #     if i <= 0 or j <= 0:
        #         return 0
        #     elif (i, j) in memo:
        #         return memo[(i, j)]
        #     elif nums1[i - 1] == nums2[j - 1]:
        #         memo[(i, j)] = 1 + solve(i - 1, j - 1)
        #     else:
        #         memo[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))
        #     return memo[(i, j)]

        # m, n = len(nums1), len(nums2)
        # memo = {}
        # return solve(m, n)