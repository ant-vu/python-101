class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(n), space: O(n)
        def helper(x):
            if x in memo:
                return memo[x]
            memo[x] = helper(x - 1) + helper(x - 2)
            return memo[x]
        memo = {1: 1, 2: 2}
        return helper(n)

        # time: O(n), space: O(1)
        # if n <= 2:
        #     return n
        # a, b = 1, 2
        # for _ in range(3, n + 1):
        #     a, b = b, a + b
        # return b

        # time: O(n), space: O(n)
        # dp = [0] * (n + 2)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]