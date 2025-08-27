class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # time: O(n + m), space: O(n + m)
        def dfs(cur, prev):
            disc[cur] = low[cur] = time[0]
            time[0] += 1
            for nxt in edgeMap[cur]:
                if not disc[nxt]:
                    dfs(nxt, cur)
                    low[cur] = min(low[cur], low[nxt])
                elif nxt != prev:
                    low[cur] = min(low[cur], disc[nxt])
                if low[nxt] > disc[cur]:
                    ans.append([cur, nxt])

        edgeMap = defaultdict(list)
        for a, b in connections:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        disc, low, time, ans = [0] * n, [0] * n, [1], []
        dfs(0, -1)
        return ans