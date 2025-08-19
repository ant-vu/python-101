class Solution:
    def fib(self, n: int) -> int:
        # time: O(n), space: O(1)
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b