class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # time: O(nlogn), space: O(1)
        points.sort()
        res = 1
        end = points[0][1]
        for i in points[1:]:
            if i[0] > end:
                res += 1
                end = i[1]
            else:
                end = min(end, i[1])
        return res

        # time: O(nlogn), space: O(n)
        # points.sort()
        # res = []
        # i = 0
        # while i < len(points):
        #     start = points[i][0]
        #     end = points[i][1]
        #     while i < len(points) - 1 and end >= points[i + 1][0]:
        #         start = max(start, points[i + 1][0])
        #         end = min(end, points[i + 1][1])
        #         i += 1
        #     res.append([start, end])
        #     i += 1
        # return len(res)