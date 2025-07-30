class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), space: O(1)
        cooldown = 0
        sell = 0
        hold = -inf
        for p in prices:
            prevCooldown = cooldown
            prevSell = sell
            prevHold = hold
            cooldown = max(prevCooldown, prevSell)
            sell = prevHold + p
            hold = max(prevHold, prevCooldown - p)
        return max(sell, cooldown)