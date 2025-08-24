class KthLargest:  # time: O((m+n)logk), space: O(k)

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if self.k > 0:
            self.k -= 1
            heapq.heappush(self.minHeap, val)
        else:
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)