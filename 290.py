class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # time: O(m + n), space: O(m + n)
        if len(pattern) != len(s.split()):
            return False
        mapping = {}
        for a, b in zip(pattern, s.split()):
            if a in mapping:
                if mapping[a] != b:
                    return False
            elif b in mapping.values():
                return False
            mapping[a] = b
        return True