class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # time: O(nlogn), space: O(n)
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        print(l)
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e[1],))
            res.append(l[r][1] if r < len(l) else -1)
        return res