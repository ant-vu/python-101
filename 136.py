class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        bit = nums[0]
        for i in range(1, len(nums)):
            bit ^= nums[i]
        return bit