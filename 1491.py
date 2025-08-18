class Solution:
    def average(self, salary: List[int]) -> float:
        # time: O(n), space: O(1)
        minS, maxS = float('inf'), float('-inf')
        for s in salary:
            minS = min(minS, s)
            maxS = max(maxS, s)
        return (sum(salary) - minS - maxS) / (len(salary) - 2)