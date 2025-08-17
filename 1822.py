class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = 1
        for n in nums:
            if n == 0:
                res *= 0
            elif n < 0:
                res *= -1
        return res