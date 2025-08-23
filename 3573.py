class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # time: O(n * k), space: O(k)
        bought = [float('-inf')] * k
        res = [0] * (k + 1)
        sold = [0] * k
        for price in prices:
            for j in range(k, 0, -1):
                res[j] = max(res[j], bought[j - 1] + price, sold[j - 1] - price)
                bought[j - 1] = max(bought[j - 1], res[j - 1] - price)
                sold[j - 1] = max(sold[j - 1], res[j - 1] + price)
        return max(res)