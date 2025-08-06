class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.refs = 0
    
    def addWord(self, word):
        cur = self
        cur.refs += 1
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.refs += 1
        cur.isEnd = True
    
    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # time: O(m + n * 4^k), space: O(m + n)
        def dfs(r, c, node, word):
            if r not in range(rows) or c not in range(cols) or board[r][c] not in node.children or node.children[board[r][c]].refs < 1 or (r, c) in visited:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                node.isEnd = False
                res.add(word)
                root.removeWord(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visited.remove((r, c))

        root = TrieNode()
        for w in words:
            root.addWord(w)
        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)