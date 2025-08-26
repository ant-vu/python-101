class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # time: O(n+m*k), space: O(1)
        res = 0
        countChars = defaultdict(int)
        for char in chars:
            countChars[char] += 1
        for word in words:
            isGood = True
            for char in word:
                if word.count(char) > countChars[char]:
                    isGood = False
                    break
            if isGood:
                res += len(word)
        return res