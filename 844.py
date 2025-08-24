class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # time: O(max(m,n)), space: O(1)
        i, j = len(s) - 1, len(t) - 1
        skipS, skipT = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS >= 1:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT >= 1:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            elif (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True

        # time: O(max(m,n)^2), space: O(max(m,n))
        # while '#' in s:
        #     if s.index('#') - 1 >= 0:
        #         s = s[:s.index('#') - 1] + s[s.index('#') + 1:]
        #     else:
        #         s = s[:s.index('#')] + s[s.index('#') + 1:]
        # while '#' in t:
        #     if t.index('#') - 1 >= 0:
        #         t = t[:t.index('#') - 1] + t[t.index('#') + 1:]
        #     else:
        #         t = t[:t.index('#')] + t[t.index('#') + 1:]
        # return s == t

        # time: O(max(m,n)), space: O(max(m,n))
        # stackS, stackT = [], []
        # for c in s:
        #     if c != '#':
        #         stackS.append(c)
        #     elif stackS:
        #         stackS.pop()
        # for c in t:
        #     if c != '#':
        #         stackT.append(c)
        #     elif stackT:
        #         stackT.pop()
        # return stackS == stackT