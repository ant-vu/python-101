class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time: O(m * n), space: O(n)
        aboveRow = [1] * n
        for _ in range(m - 1):
            curRow = [1] * n
            for c in range(1, n):
                curRow[c] = curRow[c - 1] + aboveRow[c]
            aboveRow = curRow
        return aboveRow[-1]

        # time: O(m * n), space: O(m * n)
        # grid = [[1 for _ in range(n)] for _ in range(m)]
        # for r in range(1, m):
        #     for c in range(1, n):
        #         grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        # return grid[-1][-1]