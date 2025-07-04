class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # time: O(n), space: O(n)
        def dfs(al, visited, from_node):
            change = 0
            visited[from_node] = True
            for to_node in al[from_node]:
                if not visited[abs(to_node)]:
                    change += dfs(al, visited, abs(to_node)) + (1 if to_node > 0 else 0)
            return change
        
        al = [[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])
        visited = [False] * n
        return dfs(al, visited, 0)