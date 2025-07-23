class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(n), space: O(1)
        if n <= 3:
            return n
        left = 2
        mid = 3
        for _ in range(n - 3):
            right = left + mid
            left = mid
            mid = right
        return right