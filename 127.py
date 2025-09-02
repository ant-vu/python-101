class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # time: O(n * l), space: O(n * l)
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        q.append([nextWord, length + 1])
        return 0