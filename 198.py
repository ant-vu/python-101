class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        memo = [-1] * len(nums)
        def helper(nums, i):
            if i < 0:
                return 0
            elif memo[i] >= 0:
                return memo[i]
            res = max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
            memo[i] = res
            return res
        return helper(nums, len(nums) - 1)