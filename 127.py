class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # time: O(n^2), space: O(n^2)
        s = set(wordList)
        if endWord not in s:
            return 0
        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            curWord, depth = q.popleft()
            if curWord == endWord:
                return depth
            for i in range(len(curWord)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curWord[i] != j:
                        newWord = curWord[:i] + j + curWord[i+1:]
                        if newWord in s:
                            s.remove(newWord)
                            q.append((newWord, depth + 1))
        return 0