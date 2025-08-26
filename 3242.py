class NeighborSum:  # time: O(n^2), space: O(n^2)

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.maps = {}
        for r in range(self.n):
            for c in range(self.n):
                self.maps[self.grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        total = 0
        r, c = self.maps[value]
        if r > 0:
            total += self.grid[r - 1][c]
        if r < self.n - 1:
            total += self.grid[r + 1][c]
        if c > 0:
            total += self.grid[r][c - 1]
        if c < self.n - 1:
            total += self.grid[r][c + 1]
        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        r, c = self.maps[value]
        if r > 0 and c > 0:
            total += self.grid[r - 1][c - 1]
        if r < self.n - 1 and c > 0:
            total += self.grid[r + 1][c - 1]
        if r > 0 and c < self.n - 1:
            total += self.grid[r - 1][c + 1]
        if r < self.n - 1 and c < self.n - 1:
            total += self.grid[r + 1][c + 1]
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)