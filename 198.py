class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        n = len(nums)
        if n <= 2:
            return max(nums)
        left = nums[0]
        mid = max(nums[0], nums[1])
        for i in range(2, n):
            right = max(mid, left + nums[i])
            left = mid
            mid = right
        return right

        # time: O(n), space: O(n)
        # n = len(nums)
        # if n <= 2:
        #     return max(nums)
        # dp = [nums[0]] + [max(nums[0], nums[1])] + [0] * (n - 2)
        # for i in range(2, n):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return dp[-1]