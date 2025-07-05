class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # time: O(n), space: O(1)
        res = 0
        for c in columnTitle:
            res = (res * 26) + (ord(c) - ord("A") + 1)
        return res

        # time: O(n), space: O(n)
        # tmp = []
        # res = 0
        # for c in columnTitle:
        #     tmp = [26 - (ord("Z") - ord(c))] + tmp
        # for i in range(len(tmp)):
        #     res += tmp[i] * (26 ** i)
        # return res