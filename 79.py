class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(m * n * 4^len(word)), space: O(4^len(word))
        def dfs(r, c, k):
            if k == len(word):
                return True
            elif not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
                return False
            visited.add((r, c))
            res = dfs(r - 1, c, k + 1) or dfs(r + 1, c, k + 1) or dfs(r, c - 1, k + 1) or dfs(r, c + 1, k + 1)
            visited.remove((r, c))
            return res

        rows = len(board)
        cols = len(board[0])
        visited = set()
        cnt = {}
        for ch in word:
            cnt[ch] = 1 + cnt.get(ch, 0)
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False