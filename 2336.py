class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.min_heap = []
        self.added_back = set()

    def popSmallest(self) -> int:
        # time: O(logk), space: O(k)
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.added_back.remove(smallest)
            return smallest
        val = self.cur
        self.cur += 1
        return val

    def addBack(self, num: int) -> None:
        # time: O(logk), space: O(k)
        if num < self.cur and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)