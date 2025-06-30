class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # time: O(nlogn), space: O(n)
        total = res = 0
        min_heap = []
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: -x[1]):
            heappush(min_heap, a)
            total += a
            if len(min_heap) > k:
                total -= heappop(min_heap)
            if len(min_heap) == k:
                res = max(res, total * b)
        return res