class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = 1
        l = 0
        for r in range(1, len(nums)):
            if nums[r - 1] >= nums[r]:
                l = r
            res = max(res, r - l + 1)
        return res