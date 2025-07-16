class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # time: O(n), space: O(1)
        if not ops:
            return m * n
        minA = min(op[0] for op in ops)
        minB = min(op[1] for op in ops)
        return minA * minB

        # time: O(n), space: O(1)
        # minA = minB = inf
        # for a, b in ops:
        #     minA = min(minA, a)
        #     minB = min(minB, b)
        # if minA == minB == inf:
        #     return m * n
        # return minA * minB

        # time: O(m * n), space: O(m * n), memory limit exceeded
        # mat = [[0 for cols in range(n)] for rows in range(m)]
        # for op in ops:
        #     for r in range(op[0]):
        #         for c in range(op[1]):
        #             mat[r][c] += 1
        # maxInt = 0
        # cnt = 0
        # for r in range(len(mat)):
        #     for c in range(len(mat[0])):
        #         if mat[r][c] > maxInt:
        #             maxInt = mat[r][c]
        #             cnt = 1
        #         elif mat[r][c] == maxInt:
        #             cnt += 1
        # return cnt