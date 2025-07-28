class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: O(n), space: O(n)
        mapping = {}
        for i, n in enumerate(nums):
            if target - n in mapping:
                return [i, mapping[target - n]]
            mapping[n] = i