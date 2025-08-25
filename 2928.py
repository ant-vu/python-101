class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # time: O(n^3), space: O(n^3)
        res = set()
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        res.add((i, j, k))
        return len(res)