class Solution:
    def reverseBits(self, n: int) -> int:
        # time: O(n), space: O(1)
        return int(bin(n)[2:].zfill(32)[::-1], 2)