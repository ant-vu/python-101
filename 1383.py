class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # time: O(nlogn), space: O(n)
        total = res = 0
        min_heap = []
        for a, b in sorted(list(zip(speed, efficiency)), key=lambda x: -x[1]):
            heappush(min_heap, a)
            total += a
            if len(min_heap) > k:
                total -= heappop(min_heap)
            if len(min_heap) <= k:
                res = max(res, total * b)
        return res % (10 ** 9 + 7)