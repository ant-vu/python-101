class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # time: O(m + n), space: O(m + n)
        cntr, cntm = {}, {}
        for c in ransomNote:
            cntr[c] = cntr.get(c, 0) + 1
        for c in magazine:
            cntm[c] = cntm.get(c, 0) + 1
        for k, v in cntr.items():
            if k not in cntm or cntm[k] < v:
                return False
        return True