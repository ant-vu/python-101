class MinStack:

    def __init__(self):
        self.data = []
        self.minElem = inf

    def push(self, val: int) -> None:
        # time: O(1), space: O(n)
        self.data.append((val, self.minElem))
        self.minElem = min(self.minElem, val)

    def pop(self) -> None:
        self.minElem = self.data.pop()[1]

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.minElem


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()