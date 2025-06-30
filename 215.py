class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time: O(nlogk), space: O(k)
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

        # time: O(nlogn), space: O(n)
        # nums = [-n for n in nums]
        # heapq.heapify(nums)
        # for i in range(k - 1):
        #     heapq.heappop(nums)
        # return -heapq.heappop(nums)