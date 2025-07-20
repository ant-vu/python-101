class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time: O(log(m * n)), space: O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            m = l + (r - l) // 2
            row = m // cols
            col = m % cols
            guess = matrix[row][col]
            if guess == target:
                return True
            elif guess < target:
                l = m + 1
            else:
                r = m - 1
        return False

        # time: O(log(m * n)), space: O(m * n)
        # flatten = [x for row in matrix for x in row]
        # l = 0
        # r = len(flatten) - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     if flatten[m] == target:
        #         return True
        #     elif flatten[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return False