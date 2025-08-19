class Solution:
    def tribonacci(self, n: int) -> int:
        # time: O(n), space: O(1)
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c

        # time: O(n), space: O(1)
        # if n <= 1:
        #     return n
        # elif n == 2:
        #     return 1
        # a, b, c = 0, 1, 1
        # for _ in range(n - 2):
        #     a, b, c = b, c, a + b + c
        # return c