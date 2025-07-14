class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time: O(m + n), space: O(m + n)
        res = []
        for n in nums1:
            idx = nums2.index(n)
            greaterElem = 0
            print(idx)
            for i in range(idx + 1, len(nums2)):
                print(i)
                if nums2[i] > n:
                    greaterElem = nums2[i]
                    break
            res.append(greaterElem if greaterElem else -1)
        return res