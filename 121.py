class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit