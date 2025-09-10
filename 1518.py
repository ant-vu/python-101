class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # time: O(logn), space: O(1)
        full, empty, drank = numBottles, 0, 0
        while full:
            drank += full
            empty += full
            full = empty // numExchange
            empty %= numExchange
        return drank