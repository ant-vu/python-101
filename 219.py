class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # time: O(n), space: O(n)
        seen = set()
        for i, val in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])
            if val in seen:
                return True
            seen.add(val)
        return False

        # time: O(n), space: O(n)
        # seen = {}
        # for i, val in enumerate(nums):
        #     if val in seen and i - seen[val] <= k:
        #         return True
        #     seen[val] = i
        # return False

        # time: O(n), space: O(n)
        # cur = set()
        # for n in nums[: k + 1]:
        #     if n in cur:
        #         return True
        #     cur.add(n)
        # for i in range(k + 1, len(nums)):
        #     cur.remove(nums[i - k - 1])
        #     if nums[i] in cur:
        #         return True
        #     cur.add(nums[i])
        # return False