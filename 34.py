class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # time: O(log(n)), space: O(1)
        foundTarget = False
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        l2 = 0
        r2 = len(nums) - 1
        while l2 <= r2:
            m = l2 + (r2 - l2) // 2
            if nums[m] <= target:
                if nums[m] == target:
                    foundTarget = True
                l2 = m + 1
            else:
                r2 = m - 1
        return [l, r2] if foundTarget else [-1, -1]