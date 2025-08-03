class Node:

    def __init__(self, nodeKey, nodeValue):
        self.nodeKey = nodeKey
        self.nodeValue = nodeValue
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        # time: O(1), space: O(n)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].nodeValue
        return -1
    
    def remove(self, node):
        prev = node.prev
        cur = node.next
        prev.next = cur
        cur.prev = prev
    
    def insert(self, node):
        prev = self.latest.prev
        cur = self.latest
        prev.next = node
        cur.prev = node
        node.next = cur
        node.prev = prev

    def put(self, key: int, value: int) -> None:
        # time: O(1), space: O(n)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.nodeKey]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)