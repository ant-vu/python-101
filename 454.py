class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # time: O(n^2), space: O(n^2)
        sums = defaultdict(int)
        res = 0
        for x in nums1:
            for y in nums2:
                sums[x + y] += 1
        for i in nums3:
            for j in nums4:
                res += sums[0 - (i + j)]
        return res