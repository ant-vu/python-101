class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # time: O(n), space: O(n)
        dp = defaultdict(int)
        maxScore = 0
        i = len(questions) - 1
        while i >= 0:
            point, brainpower = questions[i]
            dp[i] = max(maxScore, point + dp[i + brainpower + 1])
            maxScore = max(maxScore, dp[i])
            i -= 1
        return maxScore