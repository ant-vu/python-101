class Solution:
    def partitionString(self, s: str) -> int:
        # time: O(n), space: O(n)
        cnt = 0
        seen = set()
        i = 0
        while i < len(s):
            if s[i] in seen:
                cnt += 1
                seen = set()
            seen.add(s[i])
            i += 1
        return cnt + 1