class MyHashMap:

    def __init__(self):
        self.vals = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        # time: O(1), space: O(n)
        self.vals[key] = value

    def get(self, key: int) -> int:
        # time: O(1), space: O(n)
        return self.vals[key]

    def remove(self, key: int) -> None:
        # time: O(1), space: O(n)
        self.vals[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)