class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # time: O(n), space: O(n)
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        for c in t:
            if c not in cnt or cnt[c] == 0:
                return c
            cnt[c] -= 1