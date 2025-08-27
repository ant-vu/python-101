class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # time: O(n), space: O(n)
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        
        return max(map(dfs, range(n)))

        # time: O(n), space: O(n)
        # def dfs(i):
        #     return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        # children = [[] for _ in range(n)]
        # for i, m in enumerate(manager):
        #     if m >= 0:
        #         children[m].append(i)
        # return dfs(headID)