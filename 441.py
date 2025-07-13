
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # time: O(n), space: O(1)
        rows = 0
        cur = 1
        while n >= cur:
            n -= cur
            rows += 1
            cur += 1
        return rows