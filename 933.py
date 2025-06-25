class RecentCounter:

    def __init__(self):
        self.data = deque()

    def ping(self, t: int) -> int:
        # time: O(1), space: O(1)
        while self.data and self.data[0] < t - 3000:
            self.data.popleft()
        self.data.append(t)
        return len(self.data)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)