class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(n), space: O(n)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        # time: O(n), space: O(1)
        # if n <= 3:
        #     return n
        # prev1 = 3
        # prev2 = 2
        # cur = 0
        # for _ in range(3, n):
        #     cur = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = cur
        # return cur

        # time: O(n), space: O(n)
        # memo = {1: 1, 2: 2}
        # def recur(n):
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = recur(n - 2) + recur(n - 1)
        #     return memo[n]
        # return recur(n)