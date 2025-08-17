class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # time: O(n^3), space: O(1)
        def area(p1, p2, p3):
            return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2
        
        res = float('-inf')
        for i in range(len(points) - 2):
            for j in range(i, len(points) - 1):
                for k in range(j, len(points)):
                    res = max(res, area(points[i], points[j], points[k]))
        return res