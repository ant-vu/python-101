class Solution:
    def minInsertions(self, s: str) -> int:
        # time: O(n^2), space: O(n^2)
        @cache
        def helper(s):
            if len(s) <= 1:
                return 0
            elif s[0] == s[-1]:
                return helper(s[1:-1])
            return 1 + min(helper(s[1:]), helper(s[:-1]))
        
        return helper(s)