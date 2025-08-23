class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        buy, hold, sell = float('inf'), 0, 0
        for price in prices:
            buy = min(buy, price - hold)
            hold = sell
            sell = max(sell, price - buy)
        return sell