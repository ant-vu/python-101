class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # time: O(n^2), space: O(1)
        res = 0
        for s in stones:
            if s in jewels:
                res += 1
        return res