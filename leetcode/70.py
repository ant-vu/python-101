class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(n), space: O(n)
        memo = {1: 1, 2: 2}
        def recur(n):
            if n in memo:
                return memo[n]
            memo[n] = recur(n - 2) + recur(n - 1)
            return memo[n]
        return recur(n)