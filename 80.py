class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        l = 2
        for r in range(l, len(nums)):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
        return l

        # time: O(n), space: O(1)
        # res = len(nums)
        # for n in nums:
        #     while nums.count(n) > 2:
        #         nums.remove(n)
        #         res -= 1
        # return res