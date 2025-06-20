class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n), space: O(1)
        unique = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            res = max(r - l + 1, res)
        return res