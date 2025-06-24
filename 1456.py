class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # time: O(n), space: O(1)
        vowels = "aeiou"
        cur = sum(c in vowels for c in s[:k])
        res = cur
        for i in range(len(s) - k):
            if s[i] in vowels:
                cur -= 1
            if s[i + k] in vowels:
                cur += 1
            res = max(res, cur)
        return res