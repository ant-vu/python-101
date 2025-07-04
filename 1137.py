class Solution:
    def tribonacci(self, n: int) -> int:
        # time: O(n), space: O(1)
        if n == 0:
            return 0
        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z