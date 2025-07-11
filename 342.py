class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # time: O(n), space: O(n)
        return n in [4 ** x for x in range(15)]