class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # time: O(n^2), space: O(n)
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfComponents = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfComponents -= 1
                    uf.union_set(i, j)
        return numberOfComponents

        # time: O(n^2), space: O(n)
        # def bfs(node):
        #     visited[node] = True
        #     q = deque([node])
        #     while q:
        #         node = q.popleft()
        #         for i in range(len(isConnected)):
        #             if isConnected[node][i] == 1 and visited[i] == False:
        #                 visited[i] = True
        #                 q.append(i)

        # visited = [False] * len(isConnected)
        # numberOfComponents = 0
        # for i in range(len(isConnected)):
        #     if visited[i] == False:
        #         numberOfComponents += 1
        #         bfs(i)
        # return numberOfComponents

        # time: O(n^2), space: O(n)
        # def dfs(node):
        #     visited[node] = True
        #     for i in range(len(isConnected)):
        #         if isConnected[node][i] == 1 and visited[i] == False:
        #             dfs(i)

        # visited = [False] * len(isConnected)
        # numberOfComponents = 0
        # for i in range(len(isConnected)):
        #     if visited[i] == False:
        #         numberOfComponents += 1
        #         dfs(i)
        # return numberOfComponents