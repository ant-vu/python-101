class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time: O(nlog(k)), space: O(k)
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        return heap[0]

        # time: O(nlog(n)), space: O(1)
        # heapq.heapify(nums)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)

        # time: O(nlog(k)), space: O(k)
        # return heapq.nlargest(k, nums)[-1]