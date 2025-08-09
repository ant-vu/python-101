class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # time: O(m + n), space: O(1)
        return bin(int(a, 2) + int(b, 2))[2:]