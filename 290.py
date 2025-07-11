class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # time: O(n), space: O(n)
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        mapping = {}
        for a, b in zip(pattern, s):
            if (a in mapping and mapping[a] != b) or (a not in mapping and b in mapping.values()):
                return False
            mapping[a] = b
        return True