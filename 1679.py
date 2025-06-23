class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # time: O(nlogn), space: O(1)
        nums.sort()
        l, r = 0, len(nums) - 1
        cnt = 0
        while l < r:
            if nums[l] + nums[r] == k:
                cnt += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return cnt

        # time: O(n), space: O(n)
        # res = 0
        # cnt = {}
        # for n in nums:
        #     cnt[n] = cnt.get(n, 0) + 1
        # for n in range(len(nums)):
        #     if k - nums[n] in cnt and nums[n] in cnt:
        #         if k - nums[n] == nums[n] and cnt[k - nums[n]] < 2:
        #             continue
        #         cnt[k - nums[n]] -= 1
        #         if cnt[k - nums[n]] == 0:
        #             cnt.pop(k - nums[n])
        #         cnt[nums[n]] -= 1
        #         if cnt[nums[n]] == 0:
        #             cnt.pop(nums[n])
        #         nums[n] = float("inf")
        #         res += 1
        # return res