class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

        # time: O(n), space: O(1)
        # res = sum([x for x in range(len(nums) + 1)])
        # for n in nums:
        #     res -= n
        # return res