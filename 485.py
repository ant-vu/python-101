class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                l = r + 1
            res = max(res, r - l + 1)
        return res