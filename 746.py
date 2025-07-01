class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # time: O(n), space: O(1)
        cost.append(0)
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

        # time: O(n), space: O(1)
        # dp = [0] * (len(cost) + 1)
        # for i in range(len(cost) - 1, -1, -1):
        #     if i == len(cost) - 1:
        #         dp[i] = cost[i]
        #     else:
        #         dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        # return min(dp[0], dp[1])