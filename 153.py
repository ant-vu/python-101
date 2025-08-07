class Solution:
    def findMin(self, nums: List[int]) -> int:
        # time: O(log(n)), space: O(1)
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

        # time: O(log(n)), space: O(1)
        # if len(nums) == 1:
        #     return nums[0]
        # l = 0
        # r = len(nums) - 1
        # while True:
        #     m = l + (r - l) // 2
        #     if nums[m - 1] > nums[m]:
        #         return nums[m]
        #     elif nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m - 1