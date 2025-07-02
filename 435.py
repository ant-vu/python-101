class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # time: O(nlogn), space: O(n)
        intervals.sort()
        overlaps = 0
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                intervals[i + 1][1] = min(intervals[i + 1][1], intervals[i][1])
                overlaps += 1
        return overlaps