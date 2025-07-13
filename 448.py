class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        for n in nums:
            while nums[n - 1] != n:
                nums[n - 1], n = n, nums[n - 1]
        return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]

        # time: O(n), space: O(n)
        # return list(set(x for x in range(1, len(nums) + 1)) - set(nums))