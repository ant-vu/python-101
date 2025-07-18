class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # time: O(1), space: O(1)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True

        # time: O(81 -> 1), space: O(81 * 3 -> 1)
        # for r in board:
        #     for n in "123456789":
        #         if r.count(n) > 1:
        #             return False
        # cols = []
        # for c in range(9):
        #     col = []
        #     for r in range(9):
        #         col.append(board[r][c])
        #     cols.append(col)
        # for c in cols:
        #     for n in "123456789":
        #         if c.count(n) > 1:
        #             return False
        # boxes = [[] for i in range(9)]
        # for r in range(9):
        #     for c in range(9):
        #         if r <= 2:
        #             if c <= 2:
        #                 boxes[0].append(board[r][c])
        #             elif c <= 5:
        #                 boxes[1].append(board[r][c])
        #             else:
        #                 boxes[2].append(board[r][c])
        #         elif r <= 5:
        #             if c <= 2:
        #                 boxes[3].append(board[r][c])
        #             elif c <= 5:
        #                 boxes[4].append(board[r][c])
        #             else:
        #                 boxes[5].append(board[r][c])
        #         else:
        #             if c <= 2:
        #                 boxes[6].append(board[r][c])
        #             elif c <= 5:
        #                 boxes[7].append(board[r][c])
        #             else:
        #                 boxes[8].append(board[r][c])
        # for b in boxes:
        #     for n in "123456789":
        #         if b.count(n) > 1:
        #             return False
        # return True