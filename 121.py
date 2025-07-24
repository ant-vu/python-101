class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        maxProfit = 0
        minSeen = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minSeen)
            minSeen = min(minSeen, prices[i])
        return maxProfit