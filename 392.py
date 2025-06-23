class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # time: O(n), space: O(1)
        cur = 0
        if cur == len(s):
            return True
        for i in range(len(t)):
            if s[cur] == t[i]:
                cur += 1
            if cur == len(s):
                return True
        return False