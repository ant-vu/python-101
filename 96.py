class Solution:
    def numTrees(self, n: int) -> int:
        # time: O(n^2), space: O(n)
        uniqueTree = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniqueTree[root - 1] * uniqueTree[nodes - root]
            uniqueTree[nodes] = total
        return uniqueTree[n]