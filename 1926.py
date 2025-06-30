class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # time: O(m * n), space: O(m * n)
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        while q:
            node = q.popleft()
            if [node[0], node[1]] != entrance and (node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1):
                return node[2]
            if node[0] - 1 >= 0 and maze[node[0] - 1][node[1]] == ".":
                q.append((node[0] - 1, node[1], node[2] + 1))
                maze[node[0] - 1][node[1]] = "+"
            if node[0] + 1 <= len(maze) - 1 and maze[node[0] + 1][node[1]] == ".":
                q.append((node[0] + 1, node[1], node[2] + 1))
                maze[node[0] + 1][node[1]] = "+"
            if node[1] - 1 >= 0 and maze[node[0]][node[1] - 1] == ".":
                q.append((node[0], node[1] - 1, node[2] + 1))
                maze[node[0]][node[1] - 1] = "+"
            if node[1] + 1 <= len(maze[0]) - 1 and maze[node[0]][node[1] + 1] == ".":
                q.append((node[0], node[1] + 1, node[2] + 1))
                maze[node[0]][node[1] + 1] = "+"
        return -1