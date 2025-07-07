class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time: O(n), space: O(1)
        if len(s) != len(t):
            return False
        mapping = {}
        for a, b in zip(s, t):
            if a not in mapping and b not in mapping.values():
                mapping[a] = b
            if a in mapping and mapping[a] == b:
                continue
            return False
        return True