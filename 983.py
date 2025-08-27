class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # time: O(n), space: O(n)
        dp = [0] * (days[-1] + 1)
        dy = set(days)
        for i in range(days[-1] + 1):
            if i not in dy:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(costs[0] + dp[max(0, i - 1)], costs[1] + dp[max(0, i - 7)], costs[2] + dp[max(0, i - 30)])
        return dp[-1]