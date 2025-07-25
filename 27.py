class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # time: O(n), space: O(1)
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k

        # time: O(n), space: O(1)
        # n = len(nums)
        # l = 0
        # r = n - 1
        # while l <= r:
        #     while r >= 0 and nums[r] == val:
        #         r -= 1
        #     while l < n and nums[l] != val:
        #         l += 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        # return l