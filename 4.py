class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # time: O(log(min(m, n))), space: O(1)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        l = 0
        r = len(nums1)
        while l <= r:
            part1 = l + (r - l) // 2
            part2 = (len(nums1) + len(nums2) + 1) // 2 - part1
            maxL1 = float("-inf") if part1 == 0 else nums1[part1 - 1]
            minR1 = float("inf") if part1 == len(nums1) else nums1[part1]
            maxL2 = float("-inf") if part2 == 0 else nums2[part2 - 1]
            minR2 = float("inf") if part2 == len(nums2) else nums2[part2]
            if maxL1 <= minR2 and maxL2 <= minR1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2
                else:
                    return max(maxL1, maxL2)
            elif maxL1 > minR2:
                r = part1 - 1
            else:
                l = part1 + 1