class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # time: O(nlogn), space: O(n)
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            if a != b:
                heapq.heappush(maxHeap, -abs(a - b))
        return -maxHeap[0] if maxHeap else 0