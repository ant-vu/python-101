class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        res = [0] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res