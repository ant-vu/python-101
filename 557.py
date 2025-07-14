class Solution:
    def reverseWords(self, s: str) -> str:
        # time: O(n), space: O(n)
        res = ""
        for w in s.split():
            res += w[::-1] + " "
        return res[:-1]