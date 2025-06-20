class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # time: O(m+n), space: O(m+n)
        res = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return "".join(res)

        # time: O(m+n), space: O(m+n)
        # res = []
        # length = min(len(word1), len(word2))
        # for i in range(length):
        #     res.append(word1[i])
        #     res.append(word2[i])
        # res.extend(word1[length:])
        # res.extend(word2[length:])
        # return "".join(res)