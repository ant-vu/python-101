class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # time: O(nlogn), space: O(n)
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                nums[i] *= -1
                if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                    i += 1
            else:
                nums[i] *= -1
            k -= 1
            if k <= 0:
                return sum(nums)