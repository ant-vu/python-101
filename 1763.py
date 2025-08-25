class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # time: O(n^3), space: O(1)
        def isNice(s):
            for c in s:
                if c.lower() not in s or c.upper() not in s:
                    return False
            return True

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - i):
                if isNice(s[j:j+i+1]):
                    return s[j:j+i+1]
        return ''