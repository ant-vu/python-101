class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time: O(m + n), space: O(m + n)
        if len(s) != len(t):
            return False
        cnts1, cnts2 = {}, {}
        for i, j in zip(s, t):
            cnts1[i] = cnts1.get(i, 0) + 1
            cnts2[j] = cnts2.get(j, 0) + 1
        return cnts1 == cnts2