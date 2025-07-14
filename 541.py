class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # time: O(n), space: O(n)
        res = ""
        revFlg = True
        for i in range(0, len(s), k):
            end = min(i + k, len(s))
            if revFlg:
                res += s[i:end][::-1]
                revFlg = False
            else:
                res += s[i:end]
                revFlg = True
        return res