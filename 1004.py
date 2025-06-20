class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # time: O(n), space: O(1)
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1

        # time: O(n), space: O(1)
        # res = 0
        # zeros = 0
        # l = 0
        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         zeros += 1
        #     if nums[r] == 1 or zeros <= k:
        #         res = max(res, r - l + 1)
        #     while zeros > k:
        #         if nums[l] == 0:
        #             zeros -= 1
        #         l += 1
        # return res