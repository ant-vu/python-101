class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # time: O(n), space: O(1)
        buy, sell = float('-inf'), 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell