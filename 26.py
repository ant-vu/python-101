class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i

        # time: O(n), space: O(1)
        # left = 0
        # last = float("-inf")
        # for i in range(len(nums)):
        #     if nums[i] > last:
        #         last = nums[i]
        #         nums[left] = nums[i]
        #         left += 1
        # return left

        # time: O(n), space: O(n)
        # left = 0
        # seen = set()
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #         nums[left] = nums[i]
        #         left += 1
        # return left