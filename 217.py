class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time: O(nlogn), space: O(1)
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

        # time: O(n), space: O(n)
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False