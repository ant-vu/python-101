class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # time: O(m * n), space: O(m * n)
        q = deque()
        minutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        while q:
            r, c, minutes = q.popleft()
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                q.append((r - 1, c, minutes + 1))
                grid[r - 1][c] = 2
            if r + 1 <= len(grid) - 1 and grid[r + 1][c] == 1:
                q.append((r + 1, c, minutes + 1))
                grid[r + 1][c] = 2
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                q.append((r, c - 1, minutes + 1))
                grid[r][c - 1] = 2
            if c + 1 <= len(grid[0]) - 1 and grid[r][c + 1] == 1:
                q.append((r, c + 1, minutes + 1))
                grid[r][c + 1] = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return minutes