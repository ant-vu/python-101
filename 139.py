class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time: O(n^3 + m * k), space: O(n + m * k), n = len(s), m = len(wordDict), k = avg len word in wordDict
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]