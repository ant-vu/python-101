class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        res = 0
        mini = prices[0]
        for i in prices:
            res = max(i - mini, res)
            mini = min(i, mini)
        return res