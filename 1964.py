class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # time: O(nlogn), space: O(n)
        lis = []
        for i, x in enumerate(obstacles):
            if len(lis) == 0 or lis[-1] <= x:
                lis.append(x)
                obstacles[i] = len(lis)
            else:
                idx = bisect_right(lis, x)
                lis[idx] = x
                obstacles[i] = idx + 1
        return obstacles