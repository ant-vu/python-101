class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # time: O(logn), space: O(1)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                l2 = r2 = m
                while l2 >= 0 and nums[l2] == target:
                    l2 -= 1
                while r2 <= len(nums) - 1 and nums[r2] == target:
                    r2 += 1
                return [l2 + 1, r2 - 1]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1, -1]