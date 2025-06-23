class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # time: O(n), space: O(1)
        cur = sum(nums[:k])
        res = cur
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]
            res = max(res, cur)
        return res / k

        # time: O(n), space: O(1)
        # cur = sum(nums[:k])
        # res = cur
        # l, r = 0, k - 1
        # while r + 1 < len(nums):
        #     cur += nums[r + 1] - nums[l]
        #     res = max(res, cur)
        #     l += 1
        #     r += 1
        # return res / k