class Solution:
    def countSegments(self, s: str) -> int:
        # time: O(n), space: O(1)
        cnt = 0
        isSegment = False
        for c in s:
            if c != " ":
                isSegment = True
            else:
                if isSegment:
                    cnt += 1
                isSegment = False
        return cnt + 1 if isSegment else cnt