class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: O(n), space: O(n)
        mapping = {}
        for idx, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], idx]
            mapping[num] = idx