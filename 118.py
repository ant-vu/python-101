class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # time: O(n), space: O(n)
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for _ in range(numRows - 2):
            tmp = []
            for i in range(len(res[-1]) - 1):
                tmp.append(res[-1][i] + res[-1][i + 1])
            res.append([1] + tmp + [1])
        return res