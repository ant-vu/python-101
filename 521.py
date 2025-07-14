class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # time: O(n), space: O(n)
        resA = resB = -inf
        for i in range(len(a), 0, -1):
            if b.find(a[:i]) == -1:
                resA = i
                break
        for i in range(len(b), 0, -1):
            if a.find(b[:i]) == -1:
                resB = i
                break
        return max(resA, resB, -1)