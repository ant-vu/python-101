class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = {}, {}
        for n in nums1:
            cnt1[n] = cnt1.get(n, 0) + 1
        for n in nums2:
            cnt2[n] = cnt2.get(n, 0) + 1
        res = []
        for c in cnt1:
            if c in cnt2:
                res.extend([c] * min(cnt1[c], cnt2[c]))
        return res