class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # time: O(n^2), space: O(1)
        n = len(grid)
        top = side = front = 0
        for r in range(n):
            bestR = bestC = 0
            for c in range(n):
                if grid[r][c] > 0:
                    top += 1
                bestR = max(bestR, grid[r][c])
                bestC = max(bestC, grid[c][r])
            side += bestR
            front += bestC
        return top + side + front