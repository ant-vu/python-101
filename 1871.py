class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # time: O(n), space: O(n)
        dp = [c == "0" for c in s]
        pre = 0
        for i in range(1, len(s)):
            if i >= minJump:
                pre += dp[i - minJump]
            if i > maxJump:
                pre -= dp[i - maxJump - 1]
            dp[i] &= pre > 0
        return dp[-1]

        # time: O(n^2), space: O(n), TLE
        # n = len(s)
        # jumpable = [False] * n
        # jumpable[0] = True
        # for i in range(n):
        #     if jumpable[i] == True:
        #         for j in range(i + minJump, min(i + maxJump + 1, n)):
        #             if s[j] == "0":
        #                 jumpable[j] = True
        # return jumpable[-1]