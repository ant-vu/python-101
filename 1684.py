class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # time: O(n), space: O(n)
        res = 0
        a = set(allowed)
        for w in words:
            for c in w:
                if c not in a:
                    res += 1
                    break
        return len(words) - res