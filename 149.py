class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # time: O(n^2), space: O(n)
        points.sort()
        slope = defaultdict(int)
        M = 0
        for i, (x1, y1) in enumerate(points):
            slope.clear()
            for x2, y2 in points[i + 1:]:
                dx = x2 - x1
                dy = y2 - y1
                G = gcd(dx, dy)
                m = (dx // G, dy // G)
                slope[m] += 1
                if slope[m] > M:
                    M = slope[m]
        return M + 1