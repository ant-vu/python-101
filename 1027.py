class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # time: O(n^2), space: O(n^2)
        n = len(nums)
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                dp[j, nums[j] - nums[i]] = 1 + dp.get((i, nums[j] - nums[i]), 1)
        return max(dp.values())