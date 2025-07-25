class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        citations.sort()
        for i, c in enumerate(citations):
            if c >= len(citations) - i:
                return len(citations) - i
        return 0

        # time: O(n), space: O(n)
        # n = len(citations)
        # citationBuckets = [0] * (n + 1)
        # for c in citations:
        #     citationBuckets[min(c, n)] += 1
        # cumulativeCitations = 0
        # for h in range(n, -1, -1):
        #     cumulativeCitations += citationBuckets[h]
        #     if cumulativeCitations >= h:
        #         return h

        # time: O(n^2), space: O(1)
        # maxH = 0
        # for h in range(len(citations) + 1):
        #     count = 0
        #     for c in citations:
        #         if c >= h:
        #             count += 1
        #     if count >= h:
        #         maxH = h
        # return maxH