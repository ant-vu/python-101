class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        total = 0
        res = nums[0]
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res