class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # time: O(n), space: O(1)
        wstart = 0
        pattern = {}
        res = []
        matched = 0
        for c in p:
            if c not in pattern:
                pattern[c] = 0
            pattern[c] += 1
        for wend in range(len(s)):
            c = s[wend]
            if c in pattern:
                pattern[c] -= 1
                if pattern[c] == 0:
                    matched += 1
            if wend >= len(p) - 1:
                if matched == len(pattern):
                    res.append(wstart)
                rc = s[wstart]
                wstart += 1
                if rc in pattern:
                    if pattern[rc] == 0:
                        matched -= 1
                    pattern[rc] += 1
        return res