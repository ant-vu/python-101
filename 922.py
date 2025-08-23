class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        l, r = 0, 1
        while l < len(nums):
            while nums[l] % 2 == 1:
                nums[l], nums[r] = nums[r], nums[l]
                r += 2
            l += 2
        return nums

        # time: O(n^2), space: O(1)
        # for l in range(len(nums) - 1):
        #     if l % 2 == nums[l] % 2:
        #         continue
        #     elif l % 2 == 1 and nums[l] % 2 == 0:
        #         for r in range(l + 1, len(nums)):
        #             if nums[r] % 2 == 1:
        #                 nums[l], nums[r] = nums[r], nums[l]
        #                 break
        #     elif l % 2 == 0 and nums[l] % 2 == 1:
        #         for r in range(l + 1, len(nums)):
        #             if nums[r] % 2 == 0:
        #                 nums[l], nums[r] = nums[r], nums[l]
        #                 break
        # return nums