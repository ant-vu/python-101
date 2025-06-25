class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # time: O(n^2), space: O(n)
        rd, cd = {}, {}
        for r in grid:
            rd[tuple(r)] = rd.get(tuple(r), 0) + 1
        for c in range(len(grid[0])):
            tmp = []
            for r in range(len(grid)):
                tmp.append(grid[r][c])
            cd[tuple(tmp)] = cd.get(tuple(tmp), 0) + 1
        cnt = 0
        for i in rd.keys():
            for j in cd.keys():
                if i == j:
                    cnt += rd[i] * cd[j]
        return cnt