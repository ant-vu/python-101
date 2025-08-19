class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # time: O(n^2), space: O(1)
        triangle.reverse()
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r - 1][c], triangle[r - 1][c + 1])
        return triangle[-1][-1]