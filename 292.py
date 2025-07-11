class Solution:
    def canWinNim(self, n: int) -> bool:
        # time: O(1), space: O(1)
        return n % 4 != 0