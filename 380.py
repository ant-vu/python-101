class RandomizedSet:

    def __init__(self):
        self.data = []
        self.dataIdx = {}
        self.idx = 0

    def insert(self, val: int) -> bool:
        # time: O(1), space: O(n)
        if val in self.dataIdx:
            return False
        else:
            self.data.append(val)
            self.dataIdx[val] = self.idx
            self.idx += 1
            return True

    def remove(self, val: int) -> bool:
        # time: O(1), space: O(n)
        if val not in self.dataIdx:
            return False
        else:
            self.data.remove(val)
            del self.dataIdx[val]
            self.idx -= 1
            return True

    def getRandom(self) -> int:
        # time: O(1), space: O(n)
        return self.data[random.randint(0, self.idx - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()