class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # time: O(m * n), space: O(1)
        for r in range(len(matrix) - 1):
            for c in range(len(matrix[0]) - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True

        # time: O(m * n), space: O(m + n)
        # cands = [(r, 0) for r in range(len(matrix))] + [(0, c) for c in range(len(matrix[0]))]
        # for r, c in cands:
        #     while r + 1 < len(matrix) and c + 1 < len(matrix[0]):
        #         if matrix[r][c] != matrix[r + 1][c + 1]:
        #             return False
        #         r += 1
        #         c += 1
        # return True