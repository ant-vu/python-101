class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        buy1 = inf
        buy2 = inf
        sell1 = 0
        sell2 = 0
        for i in range(len(prices)):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2