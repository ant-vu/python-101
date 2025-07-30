class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        curMin = nums[0]
        curMax = nums[0]
        sumMin = nums[0]
        sumMax = nums[0]
        sumTot = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            sumMax = max(sumMax, curMax)
            curMin = min(curMin + nums[i], nums[i])
            sumMin = min(sumMin, curMin)
            sumTot += nums[i]
        if sumMin == sumTot:
            return sumMax
        return max(sumMax, sumTot - sumMin)