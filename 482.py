class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # time: O(n), space: O(1)
        s = s.upper().replace("-", "")[::-1]
        groups = []
        cur = ""
        for c in s:
            cur += c
            if len(cur) == k:
                groups.append(cur[::-1])
                cur = ""
        if cur:
            groups.append(cur[::-1])
        return "-".join(reversed(groups))