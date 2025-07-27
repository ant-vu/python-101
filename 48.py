class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time: O(n^2), space: O(1)
        n = len(matrix)
        top = 0
        bot = n - 1
        while top < bot:
            for c in range(n):
                matrix[top][c], matrix[bot][c] = matrix[bot][c], matrix[top][c]
            top += 1
            bot -= 1
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # time: O(n^2), space: O(n^2)
        # n = len(matrix)
        # rows = [r for r in matrix]
        # cols = []
        # for i in range(n):
        #     c = []
        #     for r in rows:
        #         c.append(r[i])
        #     cols.append(c[::-1])
        # for r in range(n):
        #     for c in range(n):
        #         matrix[r][c] = cols[r][c]