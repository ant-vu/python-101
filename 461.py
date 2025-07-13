class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # time: O(1), space: O(1)
        hamming = 0
        while x and y:
            if (x & 1) + (y & 1) == 1:
                hamming += 1
            x >>= 1
            y >>= 1
        while x:
            if x & 1 == 1:
                hamming += 1
            x >>= 1
        while y:
            if y & 1 == 1:
                hamming += 1
            y >>= 1
        return hamming