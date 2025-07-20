class Solution:
    def trailingZeroes(self, n: int) -> int:
        # time: O(logn), space: O(1)
        cnt = 0
        divisor = 5
        while n >= divisor:
            cnt += n // divisor
            divisor *= 5
        return cnt

        # time: O(n), space: O(1)
        # res = 0
        # fact = factorial(n)
        # while fact % 10 == 0:
        #     res += 1
        #     fact //= 10
        # return res