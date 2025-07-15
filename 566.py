class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # time: O(m * n), space: O(m * n)
        r2, c2 = len(mat), len(mat[0])
        if r2 * c2 != r * c:
            return mat
        res = []
        cur = []
        for row in range(r2):
            for col in range(c2):
                cur.append(mat[row][col])
                if len(cur) == c:
                    res.append(cur)
                    cur = []
        return res