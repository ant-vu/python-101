class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # time: O(1), space: O(1)
        return ((high + 1) // 2) - (low // 2)