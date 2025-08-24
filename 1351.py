class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # time: O(m + n), space: O(1)
        r, c = len(grid) - 1, 0
        res = 0
        while r >= 0 and c < len(grid[0]):
            if grid[r][c] < 0:
                r -= 1
                res += len(grid[0]) - c
            else:
                c += 1
        return res

        # time: O(mlogn), space: O(1)
        # res = 0
        # for row in grid:
        #     l, r = 0, len(row) - 1
        #     while l <= r:
        #         m = l + (r - l) // 2
        #         if row[m] < 0:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     res += len(row) - l
        # return res