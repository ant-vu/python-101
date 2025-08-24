class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # time: O(n^2), space: O(n)
        def isSorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        res = 0
        while not isSorted(nums):
            res += 1
            minSum = float('inf')
            minSumIdx = float('inf')
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    minSumIdx = i
            nums = nums[:minSumIdx] + [minSum] + nums[minSumIdx+2:]
        return res