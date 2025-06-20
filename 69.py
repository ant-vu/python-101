class Solution:
    def mySqrt(self, x: int) -> int:
        # time: O(logn), space: O(1)
        if x == 1:
            return 1
        low = 0
        high = x // 2
        while low <= high:
            mid = low + (high - low) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1
        return high