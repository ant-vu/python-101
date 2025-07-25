class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # time: O(n), space: O(n)
        if numRows == 1 or numRows >= len(s):
            return s
        row = 0
        down = 1
        arr = [[] for _ in range(numRows)]
        for c in s:
            arr[row].append(c)
            if row == 0:
                down = 1
            elif row == numRows - 1:
                down = -1
            row += down
        return "".join(["".join(x) for x in arr])

        # time: O(n^2), space: O(n)
        # if numRows == 1:
        #     return s
        # arr = ["" for _ in range(numRows)]
        # row = 0
        # down = True
        # for c in s:
        #     arr[row] += c
        #     if down:
        #         row += 1
        #         if row == numRows:
        #             down = False
        #             row -= 2
        #     else:
        #         row -= 1
        #         if row == -1:
        #             down = True
        #             row += 2
        # return "".join(arr)