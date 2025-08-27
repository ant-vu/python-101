class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # time: O(n + m), space: O(n)
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if visited[neighbor] == False:
                    stack.append(neighbor)
                    visited[neighbor] = True
        return all(visited)
        
        # time: O(n + m), space: O(n)
        # n = len(rooms)
        # visited = [False] * n
        # visited[0] = True
        # q = deque([0])
        # while q:
        #     node = q.popleft()
        #     for neighbor in rooms[node]:
        #         if visited[neighbor] == False:
        #             q.append(neighbor)
        #             visited[neighbor] = True
        # return all(visited)