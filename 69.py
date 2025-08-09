class Solution:
    def mySqrt(self, x: int) -> int:
        # time: O(n), space: O(1)
        if x == 1:
            return 1
        l = 0
        r = x // 2
        while l <= r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1
        return r