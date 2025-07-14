class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # time: O(n), space: O(n)
        return word in (word.upper(), word.lower(), word.capitalize())