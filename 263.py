class Solution:
    def isUgly(self, n: int) -> bool:
        # time: O(n), space: O(1)
        if n == 0:
            return False
        while n % 5 == 0:
            n //= 5
        while n % 3 == 0:
            n //= 3
        while n % 2 == 0:
            n //= 2
        return n == 1