class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # time: O(n^2), space: O(n)
        rows = len(triangle)
        memo = triangle[rows - 1].copy()
        for r in range(rows - 2, -1, -1):
            for c in range(r + 1):
                memo[c] = min(memo[c], memo[c + 1]) + triangle[r][c]
        return memo[0]