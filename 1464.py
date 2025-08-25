class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        max1, max2 = float('-inf'), float('-inf')
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)

        # time: O(nlogn), space: O(n)
        # maxHeap = [-n for n in nums]
        # heapq.heapify(maxHeap)
        # return (-heapq.heappop(maxHeap) - 1) * (-heapq.heappop(maxHeap) - 1)