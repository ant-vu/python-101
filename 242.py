class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time: O(m + n), space: O(m + n)
        if len(s) != len(t):
            return False
        mapS = {}
        for c in s:
            mapS[c] = mapS.get(c, 0) + 1
        for c in t:
            if c not in mapS or mapS[c] == 0:
                return False
            mapS[c] -= 1
        return True