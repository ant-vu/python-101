class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # time: O(m * n), space: O(1)
        return max(sum(row) for row in accounts)