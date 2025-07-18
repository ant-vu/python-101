class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time: O(nlogn), space: O(n)
        intervals.sort()
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

        # time: O(nlogn), space: O(n)
        # sortedIntervals = sorted(intervals)
        # res = []
        # l, r = sortedIntervals[0][0], sortedIntervals[0][1]
        # for i in range(len(sortedIntervals)):
        #     if sortedIntervals[i][0] > r:
        #         res.append([l, r])
        #         l = sortedIntervals[i][0]
        #         r = sortedIntervals[i][1]
        #     else:
        #         l = min(l, sortedIntervals[i][0])
        #         r = max(r, sortedIntervals[i][1])
        # res.append([l, r])
        # return res