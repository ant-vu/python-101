class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # time: O(n^2), space: O(1)
        for r in range(1, len(matrix)):
            matrix[r][0] += min(matrix[r - 1][0], matrix[r - 1][1])
            for c in range(1, len(matrix[0]) - 1):
                matrix[r][c] += min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r - 1][c + 1])
            matrix[r][-1] += min(matrix[r - 1][-1], matrix[r - 1][-2])
        return min(matrix[-1])