class Solution:
    def reverseWords(self, s: str) -> str:
        # time: O(n), space: O(n)
        s = s.split(" ")
        res = []
        for w in s:
            if w != "":
                res.append(w)
        return " ".join(res[::-1])