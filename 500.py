class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if set("qwertyuiop") >= set(w.lower()) or set("asdfhgjkl") >= set(w.lower()) or set("zxcvbnm") >= set(w.lower()):
                res.append(w)
        return res