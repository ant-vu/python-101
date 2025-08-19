class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # time: O(m * n), space: O(1)
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = int(matrix[r][c])
                if res == 0 and matrix[r][c] == 1:
                    res = 1
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) >= matrix[r][c] and matrix[r][c] > 0:
                    matrix[r][c] = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + 1
                    res = max(res, matrix[r][c] ** 2)
        return res