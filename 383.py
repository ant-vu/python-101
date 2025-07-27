class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # time: O(m + n), space: O(1)
        count = {}
        for c in magazine:
            count[c] = count.get(c, 0) + 1
        for c in ransomNote:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False
        return True