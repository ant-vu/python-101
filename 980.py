class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # time: O(m * n), space: O(n)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        walk = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 0:
                    walk += 1
        
        def backtrack(r, c, covered):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == -1:
                return 0
            elif covered == walk and grid[r][c] == 2:
                return 1
            original = grid[r][c]
            grid[r][c] = -1
            tmp = 0
            for dr, dc in directions:
                tmp += backtrack(r + dr, c + dc, covered + 1)
            grid[r][c] = original
            return tmp

        return backtrack(start[0], start[1], -1)