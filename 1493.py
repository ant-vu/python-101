class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        l = r = cnt = res = 0
        while r < len(nums):
            if nums[r] == 0:
                cnt += 1
            while l < r and cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            r += 1
            res = max(res, r - l - 1)
        return res