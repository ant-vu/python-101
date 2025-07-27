class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time: O(m * n), space: O(m * n)
        spiral = []
        rows = len(matrix)
        cols = len(matrix[0])
        x = 0
        y = 0
        dx = 1
        dy = 0
        for _ in range(rows * cols):
            spiral.append(matrix[y][x])
            matrix[y][x] = "*"
            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == "*":
                dx, dy = -dy, dx
            x += dx
            y += dy
        return spiral