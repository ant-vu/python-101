class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        # time: O(logn), space: O(n)
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -self.lo[0])
        heapq.heappop(self.lo)
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)

    def findMedian(self) -> float:
        # time: O(logn), space: O(n)
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (self.hi[0] - self.lo[0]) / 2

    # def __init__(self):
    #     self.data = []

    # def addNum(self, num: int) -> None:
    #     # time: O(1), space: O(n)
    #     self.data.append(num)

    # def findMedian(self) -> float:
    #     # time: O(nlog(n)), space: O(n)
    #     self.data.sort()
    #     if len(self.data) % 2 == 0:
    #         return (self.data[(len(self.data) // 2) - 1] + self.data[len(self.data) // 2]) / 2
    #     return self.data[len(self.data) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()