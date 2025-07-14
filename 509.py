class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        l, r = 0, 1
        for _ in range(n - 1):
            l, r = r, l + r
        return r