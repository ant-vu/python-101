class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res