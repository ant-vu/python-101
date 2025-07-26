class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # time: O(n), space: O(1)
        sIdx = 0
        tIdx = 0
        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]:
                sIdx += 1
            tIdx += 1
        return sIdx == len(s)