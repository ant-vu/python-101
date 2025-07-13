class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # time: O(mlogm + nlogn), space: O(m + n)
        g.sort(), s.sort()
        gIdx, sIdx = 0, 0
        contentChildren = 0
        while gIdx < len(g) and sIdx < len(s):
            if g[gIdx] <= s[sIdx]:
                contentChildren += 1
                gIdx += 1
            sIdx += 1
        return contentChildren