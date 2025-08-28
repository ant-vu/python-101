class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # time: O(m * n), space: O(1)
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'R':
                    rowR, colR = r, c
                    break
        res = 0
        upR, upC = rowR, colR
        while upR >= 0:
            if board[upR][upC] == 'p':
                res += 1
                break
            elif board[upR][upC] == 'B':
                break
            upR -= 1
        upR, upC = rowR, colR
        while upR < m:
            if board[upR][upC] == 'p':
                res += 1
                break
            elif board[upR][upC] == 'B':
                break
            upR += 1
        upR, upC = rowR, colR
        while upC >= 0:
            if board[upR][upC] == 'p':
                res += 1
                break
            elif board[upR][upC] == 'B':
                break
            upC -= 1
        upR, upC = rowR, colR
        while upC < n:
            if board[upR][upC] == 'p':
                res += 1
                break
            elif board[upR][upC] == 'B':
                break
            upC += 1
        return res