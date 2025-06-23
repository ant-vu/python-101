class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # time: O(n), space: O(n)
        res = 0
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        for n in range(len(nums)):
            if k - nums[n] in cnt and nums[n] in cnt:
                if k - nums[n] == nums[n] and cnt[k - nums[n]] < 2:
                    continue
                cnt[k - nums[n]] -= 1
                if cnt[k - nums[n]] == 0:
                    cnt.pop(k - nums[n])
                cnt[nums[n]] -= 1
                if cnt[nums[n]] == 0:
                    cnt.pop(nums[n])
                nums[n] = float("inf")
                res += 1
        return res