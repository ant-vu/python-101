class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # time: O(log(n)), space: O(1)
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return r