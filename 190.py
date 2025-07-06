class Solution:
    def reverseBits(self, n: int) -> int:
        # time: O(n), space: O(1)
        n = str(bin(n)[2:])[::-1]
        n += "0" * (32 - len(n))
        return int(n, 2)