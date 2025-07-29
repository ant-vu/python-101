class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # time: O(n), space: O(n)
        res = []
        if not nums:
            return res
        i = 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            i += 1
        return res