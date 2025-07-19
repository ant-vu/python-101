class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # time: O(n^2), space: O(n^2)
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        q = deque()
        min_rolls[1] = 0
        q.append(1)
        while q:
            x = q.popleft()
            for i in range(1, 7):
                t = x + i
                if t > n * n:
                    break
                row, col = divmod(t - 1, n)
                v = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                y = v if v > 0 else t
                if y == n * n:
                    return min_rolls[x] + 1
                elif min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)
        return -1