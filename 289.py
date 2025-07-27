class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # time: O(m * n), space: O(1)
        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        for r in range(m):
            for c in range(n):
                liveNei = 0
                for x, y in dirs:
                    if 0 <= r + x < m and 0 <= c + y < n and abs(board[r + x][c + y]) == 1:
                        liveNei += 1
                if board[r][c] == 1 and (liveNei < 2 or liveNei > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and liveNei == 3:
                    board[r][c] = 2
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

        # time: O(m * n), space: O(m * n)
        # m = len(board)
        # n = len(board[0])
        # myBoard = [[0] * n for _ in range(m)]
        # for r in range(m):
        #     for c in range(n):
        #         liveNei = 0
        #         for i in range(r - 1, r + 2):
        #             for j in range(c - 1, c + 2):
        #                 if (i != r or j != c) and 0 <= i < m and 0 <= j < n and board[i][j] == 1:
        #                     liveNei += 1
        #         if board[r][c] == 1:
        #             if liveNei < 2 or liveNei > 3:
        #                 myBoard[r][c] = 0
        #             else:
        #                 myBoard[r][c] = 1
        #         else:
        #             if liveNei == 3:
        #                 myBoard[r][c] = 1
        #             else:
        #                 myBoard[r][c] = 0
        # for r in range(m):
        #     for c in range(n):
        #         board[r][c] = myBoard[r][c]