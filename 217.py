class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time: O(n), space: O(n)
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False