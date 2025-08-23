class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

        # time: O(n), space: O(1)
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     while l < r and nums[l] % 2 == 0:
        #         l += 1
        #     while l < r and nums[r] % 2 == 1:
        #         r -= 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        # return nums