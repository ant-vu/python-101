class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        maxNum = max(nums)
        for n in nums:
            if n != maxNum and n * 2 > maxNum:
                return -1
        return nums.index(maxNum)