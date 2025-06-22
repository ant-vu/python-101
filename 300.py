class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(n^2), space: O(n)
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    dp[i] = max(dp[i], 1)
        return max(dp)