class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = max(nums)
        curMax = 1
        curMin = 1
        for n in nums:
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)
        return res