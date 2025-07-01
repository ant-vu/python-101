class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # time: O(n * t), space: O(t)
        dp = [1]
        for i in range(1, target + 1):
            dp.append(sum(dp[i - x] for x in nums if i - x >= 0))
        return dp[-1]