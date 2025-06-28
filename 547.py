class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # time: O(n^2), space: O(n)
        def dfs(node, isConnected, visit):
            visit[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    dfs(i, isConnected, visit)
        
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size
        for i in range(size):
            if not visit[i]:
                numberOfComponents += 1
                dfs(i, isConnected, visit)
        return numberOfComponents