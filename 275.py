class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # time: O(logn), space: O(1)
        n = len(citations)
        maxH = 0
        l = 0
        r = n - 1
        while l <= r:
            m = l + (r - l) // 2
            if citations[m] >= n - m:
                maxH = max(maxH, n - m)
                r = m - 1
            else:
                l = m + 1
        return maxH

        # time: O(n), space: O(1)
        # for i, c in enumerate(citations):
        #     if c >= len(citations) - i:
        #         return len(citations) - i
        # return 0