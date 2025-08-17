class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # time: O(n), space: O(n)
        clean = ''
        for c in paragraph:
            if c.isalpha():
                clean += c.lower()
            else:
                clean += ' '

        cnts = {}
        for w in clean.split():
            cnts[w] = cnts.get(w, 0) + 1

        resCnt = float('-inf')
        for k, v in cnts.items():
            if k not in banned and v > resCnt:
                res = k
                resCnt = v
        return res