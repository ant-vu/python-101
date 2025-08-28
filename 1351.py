class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # time: O(ROWS + COLS), space: O(1)
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        c = 0
        for r in range(ROWS - 1, -1, -1):
            while c < COLS and grid[r][c] >= 0:
                c += 1
            res += COLS - c
        return res