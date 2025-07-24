class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # time: O(rows * cols), space: O(rows * cols)
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        maxArea = 0
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(i)
        return maxArea