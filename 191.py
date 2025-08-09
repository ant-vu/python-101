class Solution:
    def hammingWeight(self, n: int) -> int:
        # time: O(n), space: O(1)
        return str(bin(n)[2:]).count("1")