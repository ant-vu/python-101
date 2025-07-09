class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # time: O(n), space: O(n)
        powers = [2 ** x for x in range(32)]
        return n in powers