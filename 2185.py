class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # time: O(m*n), space: O(1)
        return sum(w.startswith(pref) for w in words)

        # time: O(m*n), space: O(1)
        # res = 0
        # for w in words:
        #     if w.startswith(pref):
        #         res += 1
        # return res