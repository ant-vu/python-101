class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # time: O(m + n), space: O(n)
        def dfs(node):
            if inStack[node] == True:
                return True
            elif visited[node] == True:
                return False
            else:
                inStack[node] = True
                visited[node] = True
                for neighbor in graph[node]:
                    if dfs(neighbor) == True:
                        return True
                inStack[node] = False
                return False
        
        n = len(graph)
        visited = [False] * n
        inStack = [False] * n
        for i in range(n):
            dfs(i)
        safeNodes = []
        for i in range(n):
            if inStack[i] == False:
                safeNodes.append(i)
        return safeNodes

        # time: O(m + n), space: O(m + n)
        # n = len(graph)
        # indegree = [0] * n
        # adj = [[] for _ in range(n)]
        # for i in range(n):
        #     for node in graph[i]:
        #         adj[node].append(i)
        #         indegree[i] += 1
        # q = deque()
        # for i in range(n):
        #     if indegree[i] == 0:
        #         q.append(i)
        # safe = [False] * n
        # while q:
        #     node = q.popleft()
        #     safe[node] = True
        #     for neighbor in adj[node]:
        #         indegree[neighbor] -= 1
        #         if indegree[neighbor] == 0:
        #             q.append(neighbor)
        # safeNodes = []
        # for i in range(n):
        #     if safe[i] == True:
        #         safeNodes.append(i)
        # return safeNodes