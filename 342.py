class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # time: O(1), space: O(1)
        return log(n, 4).is_integer() if n > 0 else False

        # time: O(n), space: O(n)
        # return n in [4 ** x for x in range(16)]