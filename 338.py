class Solution:
    def countBits(self, n: int) -> List[int]:
        # time: O(m * n), space: O(n)
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = bin(i)[2:].count("1")
        return res