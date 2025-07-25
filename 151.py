class Solution:
    def reverseWords(self, s: str) -> str:
        # time: O(n), space: O(n)
        words = s.split()
        l = 0
        r = len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)

        # time: O(n), space: O(n)
        # return " ".join(s.split()[::-1])