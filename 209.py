class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        l = total = 0
        res = inf
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != inf else 0

        # time: O(n), space: O(n)
        # if sum(nums) < target:
        #     return 0
        # elif sum(nums) == target:
        #     return len(nums)
        # l, r = 0, 0
        # res, total = inf, 0
        # while r < len(nums):
        #     while total >= target:
        #         res = min(res, r - l)
        #         total -= nums[l]
        #         l += 1
        #     else:
        #         total += nums[r]
        #         r += 1
        # while total >= target:
        #     res = min(res, r - l)
        #     total -= nums[l]
        #     l += 1
        # return res