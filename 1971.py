class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # time: O(max(v,e)), space: O(max(v,e))
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        q = deque([source])
        vis = set([source])
        while q:
            s = q.popleft()
            if s == destination:
                return True
            for d in graph[s]:
                if d not in vis:
                    q.append(d)
                    vis.add(d)
        return False

        # time: O(max(v,e)), space: O(max(v,e))
        # def dfs(s):
        #     if s == destination:
        #         return True
        #     vis.add(s)
        #     for d in graph[s]:
        #         if d not in vis and dfs(d):
        #             return True
        #     return False

        # graph = defaultdict(list)
        # for s, d in edges:
        #     graph[s].append(d)
        #     graph[d].append(s)
        # vis = set()
        # return dfs(source)