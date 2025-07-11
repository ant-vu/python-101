class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # time: O(1), space: O(1)
        return (3 ** 19) % n == 0 if n > 0 else False

        # time: O(n), space: O(n)
        # return n in [3 ** x for x in range(19)]