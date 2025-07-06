class Solution:
    def reverseBits(self, n: int) -> int:
        # time: O(1), space: O(1)
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

        # time: O(1), space: O(1)
        # n = str(bin(n)[2:])[::-1]
        # n += "0" * (32 - len(n))
        # return int(n, 2)