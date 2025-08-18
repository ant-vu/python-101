class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        nums.sort()
        res = 0
        i, j, k = 0, 1, 2
        while i != len(nums) - 3 or j != len(nums) - 2 or k != len(nums) - 1:
            if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                res = max(res, nums[i] + nums[j] + nums[k])
            if i < j - 1:
                i += 1
            elif j < k - 1:
                j += 1
            else:
                k += 1
        if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
            res = max(res, nums[i] + nums[j] + nums[k])
        return res