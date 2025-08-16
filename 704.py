class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time: O(logn), space: O(1)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1