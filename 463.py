from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # time: O(m * n), space: O(1)
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if r == 0 or (r >= 1 and grid[r - 1][c] != 1):
                        perimeter += 1
                    if r == len(grid) - 1 or (r <= len(grid) - 2 and grid[r + 1][c] != 1):
                        perimeter += 1
                    if c == 0 or (c >= 1 and grid[r][c - 1] != 1):
                        perimeter += 1
                    if c == len(grid[0]) - 1 or (c <= len(grid[0]) - 2 and grid[r][c + 1] != 1):
                        perimeter += 1
        return perimeter