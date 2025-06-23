class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # time: O(n), space: O(1)
        sp = tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)

        # time: O(n), space: O(1)
        # cur = 0
        # if cur == len(s):
        #     return True
        # for i in range(len(t)):
        #     if s[cur] == t[i]:
        #         cur += 1
        #     if cur == len(s):
        #         return True
        # return False