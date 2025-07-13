class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # time: O(n^2), space: O(n)
        for i in range(1, len(s)):
            cur = ""
            while len(cur) <= len(s):
                if cur == s:
                    return True
                cur += s[:i]
        return False