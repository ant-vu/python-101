class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # time: O(n^2), space: O(n)
        res = 1
        while word * res in sequence:
            res += 1
        return res - 1