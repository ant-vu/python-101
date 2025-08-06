class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # time: O(n), space: O(m * n)
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        # time: O(n), space: O(m * n)
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        # time: O(n), space: O(m * n)
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)