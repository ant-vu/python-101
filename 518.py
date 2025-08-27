class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # time: O(amount*len(coins)), space: O(amount)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]