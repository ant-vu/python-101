class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # time: O(m * n), space: O(m * n)
        m, n = len(matrix), len(matrix[0])
        res = [[None] * m for _ in range(n)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                res[c][r] = val
        return res