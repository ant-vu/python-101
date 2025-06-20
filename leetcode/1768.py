class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # time: O(n), space: O(n)
        res = ""
        length = min(len(word1), len(word2))
        for i in range(length):
            res += word1[i]
            res += word2[i]
        res += word1[length:]
        res += word2[length:]
        return res