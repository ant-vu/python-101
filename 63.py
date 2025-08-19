class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # time: O(m * n), space: O(1)
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for r in range(1, len(obstacleGrid)):
            obstacleGrid[r][0] = obstacleGrid[r - 1][0] * (1 - obstacleGrid[r][0])
        for c in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][c] = obstacleGrid[0][c - 1] * (1 - obstacleGrid[0][c])
        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                obstacleGrid[r][c] = (obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]) * (1 - obstacleGrid[r][c])
        return obstacleGrid[-1][-1]