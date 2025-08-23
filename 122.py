class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit += sell - buy
            buy = sell
        return profit