class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # time: O(nlogn), space: O(n)
        points.sort()
        cnt = 0
        for i in range(len(points) - 1):
            if points[i][1] >= points[i + 1][0]:
                points[i + 1][0] = max(points[i + 1][0], points[i][0])
                points[i + 1][1] = min(points[i + 1][1], points[i][1])
                cnt += 1
        return len(points) - cnt