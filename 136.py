class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = nums[0]
        for n in nums[1:]:
            res ^= n
        return res