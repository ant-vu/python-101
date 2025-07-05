class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # time: O(n), space: O(n)
        tmp = []
        res = 0
        for c in columnTitle:
            tmp = [26 - (ord("Z") - ord(c))] + tmp
        for i in range(len(tmp)):
            res += tmp[i] * (26 ** i)
        return res