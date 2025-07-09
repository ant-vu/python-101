class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # time: O(1), space: O(1)
        return n > 0 and (n & (n - 1)) == 0

        # time: O(n), space: O(n)
        # powers = [2 ** x for x in range(32)]
        # return n in powers