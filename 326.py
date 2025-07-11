class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # time: O(n), space: O(n)
        return n in [3 ** x for x in range(32)]