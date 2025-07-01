class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # time: O(logn), space: O(1)
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if 0 < m < len(nums) - 1 and nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            elif nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1