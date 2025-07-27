class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time: O(n), space: O(1)
        mapping = {}
        for a, b in zip(s, t):
            if a in mapping and mapping[a] != b:
                return False
            elif a not in mapping and b in mapping.values():
                return False
            mapping[a] = b
        return True