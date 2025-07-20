class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # time: O(m * n), space: O(m * n)
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    self.bfs(grid, r, c)
        return islands
    
    def bfs(self, grid, r, c):
        m = len(grid)
        n = len(grid[0])
        grid[r][c] = "0"
        if r > 0 and grid[r - 1][c] == "1":
            self.bfs(grid, r - 1, c)
        if r < m - 1 and grid[r + 1][c] == "1":
            self.bfs(grid, r + 1, c)
        if c > 0 and grid[r][c - 1] == "1":
            self.bfs(grid, r, c - 1)
        if c < n - 1 and grid[r][c + 1] == "1":
            self.bfs(grid, r, c + 1)

        # time: O(r * c), space: O(r * c)
        # def bfs(r, c):
        #     q = deque()
        #     visited.add((r, c))
        #     q.append((r, c))
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
        #                 q.append((r, c))
        #                 visited.add((r, c))

        # islands = 0
        # visited = set()
        # rows, cols = len(grid), len(grid[0])
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             islands += 1
        #             bfs(r, c)
        # return islands