class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time: O(n), space: O(1)
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        res, has_odd = 0, False
        for v in cnt.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                has_odd = True
        return res + 1 if has_odd else res