class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # time: O(n^2), space: O(n)
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        maxLen, endIdx = 1, 0
        for i in range(1, n):
            bestLen, bestPrev = 1, -1
            for j in range(i - 1, -1, -1):
                if groups[i] != groups[j] and dp[j] + 1 > bestLen:
                    bestLen, bestPrev = dp[j] + 1, j
            dp[i] = bestLen
            prev[i] = bestPrev
            if dp[i] > maxLen:
                maxLen, endIdx = dp[i], i
        res = []
        i = endIdx
        while i != -1:
            res.append(words[i])
            i = prev[i]
        return res[::-1]

        # time: O(n), space: O(1)
        # return [words[0]] + [words[i] for i in range(1, len(words)) if groups[i] != groups[i - 1]]

        # time: O(n), space: O(n)
        # resW, resG = [], None
        # for w, g in zip(words, groups):
        #     if resG == None or resG != g:
        #         resG = g
        #         resW.append(w)
        # return resW