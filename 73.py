class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time: O(m * n), space: O(1)
        m = len(matrix)
        n = len(matrix[0])
        rZero = False
        cZero = False
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        rZero = True
                    if c == 0:
                        cZero = True
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if rZero:
            for c in range(n):
                matrix[0][c] = 0
        if cZero:
            for r in range(m):
                matrix[r][0] = 0

        # time: O(m * n), space: O(m + n)
        # m = len(matrix)
        # n = len(matrix[0])
        # rows = set()
        # cols = set()
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c] == 0:
        #             rows.add(r)
        #             cols.add(c)
        # for r in range(m):
        #     for c in range(n):
        #         if r in rows or c in cols:
        #             matrix[r][c] = 0