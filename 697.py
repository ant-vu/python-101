class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        lIdxs = {}
        rIdxs = {}
        cnts = {}
        for i, n in enumerate(nums):
            if n not in lIdxs:
                lIdxs[n] = i
            rIdxs[n] = i
            cnts[n] = cnts.get(n, 0) + 1
        deg = max(cnts.values())
        cands = [k for k, v in cnts.items() if v == deg]
        res = float('inf')
        return min([rIdxs[c] - lIdxs[c] + 1 for c in cands])