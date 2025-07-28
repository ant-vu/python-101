class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # time: O(n), space: O(n)
        lastIdx = {}
        for i, n in enumerate(nums):
            if n in lastIdx and i - lastIdx[n] <= k:
                return True
            lastIdx[n] = i
        return False