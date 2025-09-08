class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        unique = set()
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
                if n not in unique:
                    unique.add(n)
            else:
                if n in unique:
                    unique.remove(n)
        return sum(unique)