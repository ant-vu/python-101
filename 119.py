class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # time: O(n), space: O(n)
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for _ in range(rowIndex - 1):
            tmp = []
            for i in range(len(res) - 1):
                tmp.append(res[i] + res[i + 1])
            res = [1] + tmp + [1]
        return res