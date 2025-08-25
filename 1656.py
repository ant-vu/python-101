class OrderedStream:  # time: O(n), space: O(n)

    def __init__(self, n: int):
        self.data = [None] * (n + 2)
        self.idx = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        while self.data[self.idx]:
            self.idx += 1
        return self.data[idKey:self.idx]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)