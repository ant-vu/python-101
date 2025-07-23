class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # time: O(m * n), space: O(n)
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c - 1]
        return dp[-1]

        # time: O(m * n), space: O(1)
        # if obstacleGrid[-1][-1] == 1:
        #     return 0
        # if obstacleGrid == [[0]]:
        #     return 1
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # for r in range(m):
        #     for c in range(n):
        #         if obstacleGrid[r][c] == 1:
        #             obstacleGrid[r][c] = inf
        # for r in range(m):
        #     if obstacleGrid[r][0] == inf:
        #         break
        #     elif r > 0:
        #         obstacleGrid[r][0] = 1
        # for c in range(n):
        #     if obstacleGrid[0][c] == inf:
        #         break
        #     elif c > 0:
        #         obstacleGrid[0][c] = 1
        # for r in range(1, m):
        #     for c in range(1, n):
        #         if obstacleGrid[r][c] != inf and obstacleGrid[r - 1][c] != inf and obstacleGrid[r][c - 1] != inf:
        #             obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        #         elif obstacleGrid[r][c] != inf and obstacleGrid[r - 1][c] != inf:
        #             obstacleGrid[r][c] = obstacleGrid[r - 1][c]
        #         elif obstacleGrid[r][c] != inf and obstacleGrid[r][c - 1] != inf:
        #             obstacleGrid[r][c] = obstacleGrid[r][c - 1]
        # return obstacleGrid[-1][-1]