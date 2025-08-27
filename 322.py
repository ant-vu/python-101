class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # time: O(amount*len(coins)), space: O(amount)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]