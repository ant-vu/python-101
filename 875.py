class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time: O(nlogm), space: O(1)
        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in piles)
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if hours_needed(m) <= h:
                r = m
            else:
                l = m + 1
        return l