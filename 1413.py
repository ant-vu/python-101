class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        smallest = min(nums)
        return -smallest + 1 if smallest < 0 else 1