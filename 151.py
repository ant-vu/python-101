class Solution:
    def reverseWords(self, s: str) -> str:
        # time: O(n), space: O(n)
        res = []
        l, r = 0, 0
        while r < len(s):
            while l < len(s) and s[l] == " ":
                l += 1
            r = l
            while r < len(s) and s[r] != " ":
                r += 1
            if l < r:
                res.append(s[l : r])
            l = r
        res2 = ""
        for i in res[::-1]:
            res2 += i + " "
        return res2[:-1]

        # time: O(n), space: O(n)
        # s = s.split(" ")
        # res = []
        # for w in s:
        #     if w != "":
        #         res.append(w)
        # return " ".join(res[::-1])