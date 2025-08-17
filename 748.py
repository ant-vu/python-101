class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # time: O(n + m * k), space: O(k)
        cntL = {}
        for c in licensePlate:
            if c.isalpha():
                cntL[c.lower()] = cntL.get(c.lower(), 0) + 1
        res = "*" * 16
        for w in words:
            if len(w) < len(res):
                cntW = {}
                for c in w:
                    cntW[c] = cntW.get(c, 0) + 1
                isCand = True
                for k, v in cntL.items():
                    if k not in cntW or cntW[k] < v:
                        isCand = False
                if isCand:
                    res = w
        return res