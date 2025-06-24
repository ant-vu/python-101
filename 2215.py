class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # time: O(n), space: O(n)
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]