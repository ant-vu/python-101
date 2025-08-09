class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        return [int(d) for d in str(int("".join([str(d) for d in digits])) + 1)]