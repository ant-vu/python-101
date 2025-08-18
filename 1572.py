class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # time: O(n), space: O(1)
        tot = 0
        for i in range(len(mat)):
            tot += mat[i][i] + mat[i][len(mat) - i - 1]
        if len(mat) % 2 == 1:
            tot -= mat[len(mat) // 2][len(mat) // 2]
        return tot