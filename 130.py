class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # time: O(m * n), space: O(1)
        def dfs(x, y):
            board[x][y] = "!"
            for x2, y2 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == "O":
                    dfs(x2, y2)

        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "!":
                    board[r][c] = "O"

        # time: O(m * n), space: O(1)
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if (r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1) and board[r][c] == "O":
        #             q = deque()
        #             q.append((r, c))
        #             while q:
        #                 n = q.popleft()
        #                 if board[n[0]][n[1]] == "O":
        #                     board[n[0]][n[1]] = "!"
        #                     if 0 < n[0]:
        #                         q.append((n[0] - 1, n[1]))
        #                     if n[0] < len(board) - 1:
        #                         q.append((n[0] + 1, n[1]))
        #                     if 0 < n[1]:
        #                         q.append((n[0], n[1] - 1))
        #                     if n[1] < len(board[0]) - 1:
        #                         q.append((n[0], n[1] + 1))
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        #         elif board[r][c] == "!":
        #             board[r][c] = "O"