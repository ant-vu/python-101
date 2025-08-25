class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # time: O(m*n), space: O(m*n)
        splitSentence = sentence.split()
        for i in range(len(splitSentence)):
            if splitSentence[i].startswith(searchWord):
                return i + 1
        return -1