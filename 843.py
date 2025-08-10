# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # time: O(n), space: O(1)
        def pairMatches(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))
        
        def mostOverlapWord():
            cnts = [defaultdict(int) for _ in range(6)]
            for w in words:
                for i, c in enumerate(w):
                    cnts[i][c] += 1
            return max(words, key=lambda x: sum(cnts[i][c] for i, c in enumerate(x)))
        
        while words:
            choice = mostOverlapWord()
            matches = master.guess(choice)
            if matches == 6:
                return
            words = [w for w in words if pairMatches(choice, w) == matches]