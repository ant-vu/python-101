class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        if len(nums) == 0:
            return 0
        left = 0
        right = 0
        for n in nums:
            left, right = right, max(right, left + n)
        return right

        # time: O(n), space: O(1)
        # if len(nums) == 0:
        #     return 0
        # memo = [-1] * (len(nums) + 1)
        # memo[0] = 0
        # memo[1] = nums[0]
        # for i in range(1, len(nums)):
        #     memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
        # return memo[len(nums)]

        # time: O(n), space: O(n)
        # memo = [-1] * len(nums)
        # def helper(nums, i):
        #     if i < 0:
        #         return 0
        #     elif memo[i] >= 0:
        #         return memo[i]
        #     res = max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
        #     memo[i] = res
        #     return res
        # return helper(nums, len(nums) - 1)