class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # time: O(n), space:(1)
        buy, sell = float("-inf"), 0
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        return sell