class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time: O(n^3 + m * k), space: O(n + m * k)
        wordSet = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]

        # time: O(n * m * k), space: O(n)
        # dp = [False] * len(s)
        # for i in range(len(s)):
        #     for w in wordDict:
        #         if i < len(w) - 1:
        #             continue
        #         if i == len(w) - 1 or dp[i - len(w)] == True:
        #             if s[i-len(w)+1:i+1] == w:
        #                 dp[i] = True
        #                 break
        # return dp[-1]

        # time: O(n * m * k), space: O(n)
        # @cache
        # def dp(i):
        #     if i < 0:
        #         return True
        #     for w in wordDict:
        #         if s[i-len(w)+1:i+1] == w and dp(i - len(w) == True):
        #             return True
        #     return False
        # return dp(len(s) - 1)

        # time: O(n^3 + m * k), space: O(n + m * k)
        # wordSet = set(wordDict)
        # q = deque([0])
        # vis = set()
        # while q:
        #     i = q.popleft()
        #     if i == len(s):
        #         return True
        #     for j in range(i + 1, len(s) + 1):
        #         if j not in vis and s[i:j] in wordSet:
        #             q.append(j)
        #             vis.add(j)
        # return False

        # time: O(n^2 * m), space: O(n * m)
        # matches = []
        # for w in wordDict:
        #     for i in range(len(s) - len(w) + 1):
        #         if s[i:i+len(w)] == w:
        #             matches.append((i, i + len(w)))
        # matches.sort()
        # dp = [True] + [False] * len(s)
        # for i, j in matches:
        #     if dp[i] == True:
        #         dp[j] = True
        # return dp[-1]