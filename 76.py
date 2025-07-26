class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # time: O(m + n), space: O(m + n)
        if len(s) < len(t):
            return ""
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        tRemaining = len(t)
        minWindow = (0, inf)
        startIdx = 0
        for endIdx, c in enumerate(s):
            if tCount[c] > 0:
                tRemaining -= 1
            tCount[c] -= 1
            if tRemaining == 0:
                while True:
                    startChar = s[startIdx]
                    if tCount[startChar] == 0:
                        break
                    tCount[startChar] += 1
                    startIdx += 1
                if endIdx - startIdx < minWindow[1] - minWindow[0]:
                    minWindow = (startIdx, endIdx)
                tCount[s[startIdx]] += 1
                tRemaining += 1
                startIdx += 1
        if minWindow[1] == inf:
            return ""
        return s[minWindow[0]:minWindow[1]+1]