class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: O(n), space: O(n)
        seenToIdx = {}
        for i, n in enumerate(nums):
            if target - n in seenToIdx:
                return [i, seenToIdx[target - n]]
            seenToIdx[n] = i