class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # time: O(n), space: O(n)
        res = []
        for i in intervals:
            if newInterval[1] < i[0]:
                res.append(newInterval)
                newInterval = i
            elif newInterval[0] > i[1]:
                res.append(i)
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        res.append(newInterval)
        return res

        # time: O(nlogn), space: O(n)
        # intervals.append(newInterval)
        # intervals.sort()
        # res = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if res[-1][1] >= intervals[i][0]:
        #         res[-1][1] = max(res[-1][1], intervals[i][1])
        #     else:
        #         res.append(intervals[i])
        # return res